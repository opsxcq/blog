+++
date = "2018-09-12T00:00:00Z"
title = "Mining monero using live a live usb linuxkit build"
tags = ["cryptography", "monero", "cryptocurrency", "mining", "devops"]
draft = true
+++

# Create the yml

# Patch the kernel

```
CONFIG_USB_XHCI_HCD=y
CONFIG_USB_XHCI_PCI=y
CONFIG_USB_EHCI_HCD=y
CONFIG_USB_EHCI_PCI=y
CONFIG_USB_OHCI_HCD=y
CONFIG_USB_OHCI_HCD_PCI=y
CONFIG_USB_UHCI_HCD=y

CONFIG_USB_STORAGE=y
CONFIG_USB_STORAGE_REALTEK=y
CONFIG_REALTEK_AUTOPM=y
CONFIG_USB_STORAGE_DATAFAB=y
CONFIG_USB_STORAGE_FREECOM=y
CONFIG_USB_STORAGE_ISD200=y
CONFIG_USB_STORAGE_USBAT=y
CONFIG_USB_STORAGE_SDDR09=y
CONFIG_USB_STORAGE_SDDR55=y
CONFIG_USB_STORAGE_JUMPSHOT=y
CONFIG_USB_STORAGE_ALAUDA=y
CONFIG_USB_STORAGE_ONETOUCH=y
CONFIG_USB_STORAGE_KARMA=y
CONFIG_USB_STORAGE_CYPRESS_ATACB=y
CONFIG_USB_STORAGE_ENE_UB6250=y
CONFIG_USB_UAS=y
```

Create a config

Clone linuxkit repository from github and go into the `kernel` folder.

```
make kconfig
```

In case you get this error:

```raw
ERRO[0008] Can't add file /home/j/test/linuxkit/kernel/README.md to tar: io: read/write on closed pipe 
ERRO[0008] Can't close tar writer: io: read/write on closed pipe 
error during connect: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.38/build?buildargs=%7B%22KERNEL_VERSIONS%22%3A%22+4.18.11+4.14.73+4.14.63+4.9.130+4.4.159%22%7D&cachefrom=%5B%5D&cgroupparent=&cpuperiod=0&cpuquota=0&cpusetcpus=&cpusetmems=&cpushares=0&dockerfile=Dockerfile.kconfig&labels=%7B%7D&memory=0&memswap=0&networkmode=default&nocache=1&rm=1&shmsize=0&t=linuxkit%2Fkconfig&target=&ulimits=null&version=1: you are not authorized to perform this operation: server returned 401.
Makefile:281: recipe for target 'kconfig' failed
make: *** [kconfig] Error 1
```

Just run

```shell
service docker stop
rm /var/lib/docker/network/files/local-kv.db
service docker start
```

Continue

https://github.com/linuxkit/linuxkit/blob/master/docs/kernels.md

# Build

```
linuxkit build -format iso-bios name-yml.file
```

# Boot to test inside qemu

## Test the image

sudo /home/opsxcq/gopath/bin/linuxkit run qemu --publish 5555:22 -iso sshd.iso

## Test the bootable pendrive inside qemu


sudo /home/opsxcq/gopath/bin/linuxkit run qemu --publish 5555:22 -iso sshd.iso
qemu-system-x86_64 -usb -usbdevice disk:/dev/sde

# References

- [Working with kernels on LinuxKit](https://github.com/linuxkit/linuxkit/blob/master/docs/kernels.md)
- [Using foreign kernels with linux kit](https://github.com/linuxkit/linuxkit/tree/master/contrib/foreign-kernels)
