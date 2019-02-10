Title: Ansible basics 
Date: 2019-01-12 19:00
tags: linux, DevOps

In this article I will dump some really simple Ansible notes to get you up and running.
So I make a simple playbook.yml

```

- name: copy a simple bash script and run it
  hosts: hosts
  remote_user: user
  tasks:
  - name: copy script
    copy: src=/home/user/script.sh dest=/root/script.sh
  - name: make the script executable
    command: chmod +x /root/script.sh
  - name: run the script
    command: /root/script.sh

```

Ansible playbook is a YAML instruction file of what tasks you want to perform on what hosts.
our hosts are defined in an inventory file, which is basically going to be a list of 
hosts we want to perform tasks on and some extra parameters.

here is the inventory file: 

```

[hosts]

[hosts]

host[1:10].company.com


[hosts:vars]
ansible_become=true
ansible_user=root

```

above is a really basic inventory file named "hosts" which we call in playbook.yml.
host[1:10] is a way we can define a range of numbers to avoid repeating ourselves e.g. host1,host2,host3. when you
run the playbook against this inventory file it will ssh into the hosts you defined. 

if you need to use a password as opposed to SSH key:

```
ansible_user=user
ansible_ssh_pass=password

``` 
command to run the playbook:

```
ansible-playbook -i hosts playbook.yml
```

now ansible will systematically run through each server you defined in hosts and perform the task. in this case
ssh onto the server, copy a bash script, make the script executable and run it.

remember to fully test any scripts you run and don't try this at home (in production) if you aren't sure
of the results.

























































