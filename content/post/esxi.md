---
title: "ESXi notes"
date: "2020-02-02T00:00:00Z"
draft: true 
tags: ["vmware","virtualization","qemu","ansible","esxi"]
---

# SSH Configuration

To upload your ssh key run:

```
cat ~/.ssh/id_rsa.pub | ssh root@10.1.1.11 'cat >> /etc/ssh/keys-root/authorized_keys'
```