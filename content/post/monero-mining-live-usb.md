+++
date = "2018-09-12T00:00:00Z"
title = "Mining monero using live a live usb linuxkit build"
tags = ["cryptography", "monero", "cryptocurrency", "mining", "devops"]
draft = true
+++

# Create the yml

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
