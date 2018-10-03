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
