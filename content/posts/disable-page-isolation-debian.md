+++
title = "How to disable page table isolation on Debian"
author = ["OPSXCQ"]
date = 2018-08-09
draft = false
+++

After meltdown, spectre and other similar bugs were discoreved and patched the
overall performance on Linux decreased. [Here a detailed benchmark](https://gist.github.com/bobrik/c67189e88efcc2a1491c54c15f5fe006) about the
impact of these fixes on Redis performance. Something between **15%** and **6%** slower
than the same machine without the fixes.

<!--more-->


## Check your linux {#check-your-linux}

To check if the fixes are enabled run the command bellow:

```bash
grep CONFIG_PAGE_TABLE_ISOLATION=y /boot/config-`uname -r` && echo "enabled" || echo "disabled"
grep -q "cpu_insecure\|cpu_meltdown\|kaiser" /proc/cpuinfo && echo "enabled" || echo "disabled"
sudo dmesg | grep -q "Kernel/User page tables isolation: enabled" && echo "enabled" || echo "disabled"
```

You can also check your system using this [exploit](https://github.com/opsxcq/exploit-cve-2017-5715). If your system is vulnerable
and has no fixes enabled, the output will be:

```text
taskset -c 1 ./exploit

[+] Testing for Spectre
[+] Dumping memory from 0xffffffffffdfeea8 to 0xffffffffffdfeec2
[+] Dumped bytes match the expected value
[+] System vulnerable to spectre
```


## Test before applying {#test-before-applying}

Before testing the fixes permanently you **should test them**, reboot your system
and edit your _grub_ configuration by pressing **E** and add these parameters to your
kernel.

```text
spectre_v2=off pti=off kpti=off
```


## Applying the fix {#applying-the-fix}

To apply these configurations permanently edit your `/etc/default/grub` file and
append the parameters above to the `GRUB_CMDLINE_LINUX_DEFAULT` line. After that
just update your grub configuration with `sudo update-grub`.


## Conclusion {#conclusion}

It is not a good idea to disable these protections on your servers, not even on
your desktop. Remember that this bug can be exploited even via Firefox. But
sometimes you need some extra performance and are willing to accept the risk.


## References {#references}

-   [Spectre website](https://spectreattack.com/)
-   [Firefox mitigations for Spectre](https://blog.mozilla.org/security/2018/01/03/mitigations-landing-new-class-timing-attack/)
