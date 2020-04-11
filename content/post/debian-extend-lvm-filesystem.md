---
title: "Extending a LVM filesystem on a Luks partition"
date: "2020-02-02T00:00:00Z"
draft: true 
tags: ["filesystem","encryption","debian","luks"]
---

- Add a another physical volume to the machine
- Initialize the disk with luks
- Add to the logical volume
- Expand the disk space

# Analysing the current state of the system

### List physical volumes

Physical volumes are volumes where you can create the base for everything else.
As seen, the new disk is not yet added here.

```shell
#pvs
  PV                     VG      Fmt  Attr PSize  PFree
  /dev/mapper/sda5_crypt vg_base lvm2 a--  15.74g    0 
```

### List Volume Groups

```shell
#vgs
  VG      #PV #LV #SN Attr   VSize  VFree
  vg_base   1   5   0 wz--n- 15.74g    0 
```


### List Logical Volumes
```shell
#lvs
  LV        VG      Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv_data   vg_base -wi-ao----   7.55g                                                    
  lv_rootfs vg_base -wi-ao----   6.05g                                                    
  lv_swap   vg_base -wi-ao---- 488.00m                                                    
  tmp       vg_base -wi-ao---- 316.00m                                                    
  var       vg_base -wi-ao----  <1.36g  
```

### Check the new disk

```shell
#fdisk -l /dev/sdb
Disk /dev/sdb: 1 TiB, 1099511627776 bytes, 2147483648 sectors
Disk model: Virtual disk    
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

# Initialize the new disk

To properly use the new disk is required some initialization with luks. It
requires to install luks (`apt install cryptsetup`) but if you use [this ansible
role](https://github.com/opsxcq/ansible-role-linux-server) you are good to go !

### Initialize the disk

```shell
#cryptsetup -y -v luksFormat /dev/sdb

WARNING!
========
This will overwrite data on /dev/sdb irrevocably.

Are you sure? (Type uppercase yes): YES
Enter passphrase for /dev/sdb: 
Verify passphrase: 
Key slot 0 created.
Command successful.
```

### Add to fstab and cryptab

Find the disk *UUID*

```shell
#ls -lha /dev/disk/by-uuid/
total 0
drwxr-xr-x 2 root root 200 Apr  9 21:38 .
drwxr-xr-x 7 root root 140 Apr  4 23:24 ..
lrwxrwxrwx 1 root root  10 Apr  4 23:24 2c93dc79-3126-41e7-b003-6a0b3e9cf254 -> ../../dm-5
lrwxrwxrwx 1 root root  10 Apr  4 23:24 3937adf5-738a-40d2-9e59-6c58a0a43f0d -> ../../dm-1
lrwxrwxrwx 1 root root  10 Apr  4 23:24 721b8db6-7904-49ad-bc34-f86390641bac -> ../../sda5
lrwxrwxrwx 1 root root  10 Apr  4 23:24 999a3dee-a954-4b29-a218-0815de1c6960 -> ../../dm-2
lrwxrwxrwx 1 root root   9 Apr  9 21:38 b4c6c266-c320-433c-981c-ed7ac3fd661f -> ../../sdb
lrwxrwxrwx 1 root root  10 Apr  4 23:24 c7839e03-8e62-4e4d-8640-c8aed269c16b -> ../../sda1
lrwxrwxrwx 1 root root  10 Apr  4 23:24 e30bd110-e05b-4239-93c6-3855e29aa2da -> ../../dm-3
lrwxrwxrwx 1 root root  10 Apr  4 23:24 f9fe8d1c-2832-4879-8593-ecf6a75e26a5 -> ../../dm-4
```

Then add it to `/etc/cryptab`

```shell
echo sdb_crypt UUID=b4c6c266-c320-433c-981c-ed7ac3fd661f none luks,discard >> /etc/crypttab
```

The resulting file should look similar total

```shell
#cat /etc/crypttab 
sda5_crypt UUID=721b8db6-7904-49ad-bc34-f86390641bac none luks,discard
sdb_crypt UUID=b4c6c266-c320-433c-981c-ed7ac3fd661f none luks,discard
```

Now mount the disk to continue with the setup:

```shell
#cryptsetup luksOpen /dev/sdb sdb_crypt
Enter passphrase for /dev/sdb: 
```

# Add new disk to LVM

### Setup physical volume

Create a physical volume on the new disk

```shell
#pvcreate /dev/mapper/sdb_crypt 
  Physical volume "/dev/mapper/sdb_crypt" successfully created.
```

Check the result with

```shell
#pvs
  PV                     VG      Fmt  Attr PSize    PFree   
  /dev/mapper/sda5_crypt vg_base lvm2 a--    15.74g       0 
  /dev/mapper/sdb_crypt          lvm2 ---  1023.98g 1023.98g
```

Or with some more advanced output

```shell
#pvdisplay
  --- Physical volume ---
  PV Name               /dev/mapper/sda5_crypt
  VG Name               vg_base
  PV Size               15.74 GiB / not usable 2.00 MiB
  Allocatable           yes (but full)
  PE Size               4.00 MiB
  Total PE              4030
  Free PE               0
  Allocated PE          4030
  PV UUID               XnUPnL-39HC-X0o7-1Nia-1MfP-W1Tm-Ealm01
   
  "/dev/mapper/sdb_crypt" is a new physical volume of "1023.98 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/mapper/sdb_crypt
  VG Name               
  PV Size               1023.98 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               fer6By-NAtM-IoHt-pOoO-MwDm-OxWL-PdzkMG
```

### Add to Volume group

List the current volume groups

```shell
#vgs
  VG      #PV #LV #SN Attr   VSize  VFree
  vg_base   1   5   0 wz--n- 15.74g    0 
  
```

Or with some more extensive and detailed output

```shell
#vgdisplay
  --- Volume group ---
  VG Name               vg_base
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  12
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                5
  Open LV               5
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               15.74 GiB
  PE Size               4.00 MiB
  Total PE              4030
  Alloc PE / Size       4030 / 15.74 GiB
  Free  PE / Size       0 / 0   
  VG UUID               YIq2D4-16pr-xvun-0kCB-GhQS-W95Q-d7UvVo
```

Extend the `vg_base` volume group bytes

```shell
#vgextend vg_base /dev/mapper/sdb_crypt
  Volume group "vg_base" successfully extended
```

Check the if the volume group was extended as expected

```shell
#vgdisplay
  --- Volume group ---
  VG Name               vg_base
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  13
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                5
  Open LV               5
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               <1.02 TiB
  PE Size               4.00 MiB
  Total PE              266169
  Alloc PE / Size       4030 / 15.74 GiB
  Free  PE / Size       262139 / 1023.98 GiB
  VG UUID               YIq2D4-16pr-xvun-0kCB-GhQS-W95Q-d7UvVo
   
```

It also shows how many *physical extent* free we have, this data is shown as
**Free PE** with the value **262139**.

Or with `pvscan` to see which volume groups are under which physical volumes

```shell
#pvscan
  PV /dev/mapper/sda5_crypt   VG vg_base         lvm2 [15.74 GiB / 0    free]
  PV /dev/mapper/sdb_crypt    VG vg_base         lvm2 [1023.98 GiB / 1023.98 GiB free]
  Total: 2 [<1.02 TiB] / in use: 2 [<1.02 TiB] / in no VG: 0 [0   ]
```

The target lv for the extension will be `/data` which we can determine the
`lv_data` name from the command

```shell
#lvs
  LV        VG      Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv_data   vg_base -wi-ao----   7.55g                                                    
  lv_rootfs vg_base -wi-ao----   6.05g                                                    
  lv_swap   vg_base -wi-ao---- 488.00m                                                    
  tmp       vg_base -wi-ao---- 316.00m                                                    
  var       vg_base -wi-ao----  <1.36g                                                    
```

Finally resizing the disk

```shell
#lvextend -l +262139 /dev/vg_base/lv_data 
  Size of logical volume vg_base/lv_data changed from 7.55 GiB (1933 extents) to <1.01 TiB (264072 extents).
  Logical volume vg_base/lv_data successfully resized.
```

Again to check the changes

```shell
#lvs
  LV        VG      Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lv_data   vg_base -wi-ao----  <1.01t                                                    
  lv_rootfs vg_base -wi-ao----   6.05g                                                    
  lv_swap   vg_base -wi-ao---- 488.00m                                                    
  tmp       vg_base -wi-ao---- 316.00m                                                    
  var       vg_base -wi-ao----  <1.36g                                                    
```

As can be stated, the volume mounted on `/data` (`lv_data`) was increased in
*1tb*, but **not the filesystem**.

```shell
#df -h /data/
Filesystem                   Size  Used Avail Use% Mounted on
/dev/mapper/vg_base-lv_data  7.6G  1.4G  6.3G  18% /data
```

For normal filesystems it would be

```shell

```

But the partition this partition uses `XFS`, so the command issues

```shell
#xfs_growfs /data
meta-data=/dev/mapper/vg_base-lv_data isize=512    agcount=4, agsize=494848 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=0
data     =                       bsize=4096   blocks=1979392, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 1979392 to 270409728
```

Verifying the filesystem size with

```shell
#df -h /data
Filesystem                   Size  Used Avail Use% Mounted on
/dev/mapper/vg_base-lv_data  1.1T  2.4G  1.1T   1% /data
#
```


# References

- [LVM Anatomy](http://tldp.org/HOWTO/LVM-HOWTO/anatomy.html)
