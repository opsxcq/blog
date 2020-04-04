---
title: "Packer notes"
date: "2020-02-02T00:00:00Z"
draft: true 
tags: ["packer","virtualization","qemu","ansible","esx"]
---

# Debug

- Set `headless: false`
- To release the mouse/keyboard from qemu, `Ctrl+Alt+G`

# Dealing with Luks

The strategy is to add a keyfile and store it on `/boot`, this way the system
will be able to boot without a password and packer will be able to run ansible
to provision the other part of the setup.

> This is a work around, and this file should be removed when the machine is
> deployed

# Running on ESXi

Connect to the ssh and run

```
esxcli system settings advanced set -o /Net/GuestIPHack -i 1
```

# Convert to ESXi

To make it compatible with ESXi just run

```
qemu-img convert -f qcow2 -O vmdk -o adapter_type=lsilogic,subformat=streamOptimized,compat6 debian10-template output.vmdk
```

> Important note, the generated disk uses IDE as controller, remember this when
> importing to ESXi

# References

- (Setup Luks with static key)[https://dradisframework.com/support/guides/customization/auto-unlock-luks-encrypted-drive.html]
