Title: open tcp socket directly in script
Date: 2018-07-02 15:24
tags: linux, bash, scripting, automation, security

    #!/bin/bash
    for host in $hosts
    do
    timeout 5 bash -c "</dev/tcp/$host/$port"
    #124 exit status means connection unsuccessful
    if [ $? -eq 124 ]
    then
        echo "cannot connect to $host:$port"
    else
        echo " successful connection to $host:$port"
    fi
    done

testing specific port on multiple hosts using direct tcp socket in absence of nmap,
telnet and netcat
