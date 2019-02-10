Title: some dodgy bash loop to SSH to a lot of servers (note: ansible would be better)
Date: 2018-07-02 14:59
tags: linux, bash, scripting, automation

this is in absence of anything else. e.g. salt, ansible.

    #!/bin/bash
    # SSH connectivity && authentication checks

    while read host; do
        echo "$host" >> ssh_output.txt ;  ssh -T -o ConnectTimeout=10 -o PasswordAuthentication=no $host 2>>ssh_output.txt
    done < servers.txt

you could add more commands to this if you wish.
