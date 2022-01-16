+++
title = "Mining monero using live a live usb linuxkit build"
author = ["OPSXCQ"]
date = 2018-09-12
draft = false
+++

Linuxkit is a good tool to create immutable Linux systems, so why don't use it
to build a Monero mining live distro ? The only thing needed to build an Linux
with Linuxkit is a `yml` file containing the system information.

<!--more-->

It can be divided in 5 main sections:

-   kernel
-   init
-   onboot - applications that will run when the Linux boot (after init)
-   services - services that will run on this system
-   files - any extra files that you need to copy into your iso (like keys or configs)

Based on these principles, bellow is the configuration of a miner that will boot
and start mining rigth away. Considering that the USB disk will be at `/dev/sdb1`
(it will work if the target machine has only one disk).


## Source {#source}

The source code is just a simple `Yaml` file

```yaml
kernel:
  image: nuald/kernel:4.12.14-extra
  cmdline: "console=tty0 root=/dev/sdb1 rootwait vga=791"
init:
  - linuxkit/init:6eb0158059b056a1567236280880cb87f03ff008
  - linuxkit/runc:6cf26a0403376de3b5396cb676b88eea4f37aff8
  - linuxkit/containerd:d955db7cd28dbd7be8a17d7063cc6b7f1bf91f0a
  - linuxkit/ca-certificates:v0.6
onboot:
  - name: sysctl
    image: linuxkit/sysctl:v0.6
  - name: rngd1
    image: linuxkit/rngd:v0.6
    command: ["/sbin/rngd", "-1"]
  - name: ram-disk
    image: linuxkit/mount:v0.6-amd64
    command: ["mount", ]
  - name: usb-storage
    image: linuxkit/modprobe:v0.6-amd64
    command: ["modprobe", "usb_storage"]
services:
  - name: getty
    image: linuxkit/getty:v0.6
    env:
     - INSECURE=true
  - name: rngd
    image: linuxkit/rngd:v0.6
  - name: dhcpcd
    image: linuxkit/dhcpcd:v0.6
  - name: sshd
    image: linuxkit/sshd:v0.6
  - name: monero-miner
    image: strm/xmrig
    command: ["/bin/xmrig", "-a", "cryptonight", "-o", "stratum+tcp://104.140.201.42:5555", "-p", "Miner01-Kit", "-k", "--donate-level=1", "--cpu-priority", "0", "-u", "YOUR_ADDRESS_HERE"]
files:
  - path: root/.ssh/authorized_keys
    source: ~/.ssh/id_rsa.pub
    mode: "0600"
    optional: true
trust:
  org:
    - linuxkit
```


## Build {#build}

To build the image above just run:

```bash
linuxkit build -format iso-bios monero-miner-live-usb.yml
```

And it will create a `.iso` file that can be copied (`dd`) to a USB disk and boot on
bare metal.


## Boot to test inside qemu {#boot-to-test-inside-qemu}

You can test your image with **qemu** if you want to be sure that everything is
working, just run:

```bash
linuxkit run qemu --publish 5555:22 -iso monero-miner-live-usb.iso
```

Then ssh to your localhost at port 5555. If you want to test if your USB disk is
working properly, run:

```bash
qemu-system-x86_64 -usb -usbdevice disk:/dev/sde
```


## References {#references}

-   [Working with kernels on LinuxKit](https://github.com/linuxkit/linuxkit/blob/master/docs/kernels.md)
-   [Using foreign kernels with linux kit](https://github.com/linuxkit/linuxkit/tree/master/contrib/foreign-kernels)
-   [How to compile new Kernels for Linuxkit](https://collabnix.com/building-your-own-customised-kernel-with-linuxkit/)
