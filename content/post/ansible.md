---
title: "Ansible notes"
date: "2020-02-02T00:00:00Z"
draft: true 
tags: ["ansible","ansible-roles","devops","docker"]
---

# 

# Creating an Ansible Role

```bash
ansible-galaxy init linux-server
```

Edit role metadata located in `meta/main.yml`, as the example

```yml
galaxy_info:
  author: OPSXCQ
  role_name: linux_server
  description: Linux server configuration
  company: STRM
  license: GPLv3
  min_ansible_version: 2.4
  platforms:
   - name: Debian
     versions:
       - jessie
       - stretch
       - buster
  galaxy_tags: [linux, server]
```

> The value of role_name will be converted to lowercase, and ‘-‘ and ‘.’ will be
> translated to ‘_’.

## Testing the role

Create a file at `tests/test.yml` with a content similar to this:

```yml
- hosts: all
  vars:
    hostname: "server.strm.sh"
    ip: "192.168.0.16"
    static_hosts: "{{ lookup('file', 'hosts') }}"
    gpg: "{{ lookup('file', 'gpg.pub') }}"
    ssh:
      authorized_keys: "{{ lookup('file', 'authorized_keys') }}"
      known_hosts: "{{ lookup('file', 'known_hosts') }}"
  tasks:
  - debug:
        msg: "Your other tasks here"
  roles:
    - ../..
```

Notice the **../..** on the role reference. To run, you can start:

```
docker run --rm -it \
        -v "$(pwd):/code" \
        -v "$HOME/.ssh/:/home/devops/.ssh/" \
        -v "$HOME/.sekretz/gcloud/:/home/devops/.config/gcloud" \
        -v "$HOME/.kube/:/home/devops/.kube/" \
        -e VAULT_PASSWORD \
        -e AWS_ACCESS_KEY_ID \
        -e AWS_SECRET_ACCESS_KEY \
        -w /code \
        --entrypoint ansible-playbook \
        strm/devops -u root -i 192.168.0.135, tests/test.yml
```

# References

- [Ansible Docs - Creating roles](https://galaxy.ansible.com/docs/contributing/creating_role.html)
