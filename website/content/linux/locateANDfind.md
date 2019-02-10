Title: A refresher on Find and Locate
Date: 2018-05-20 23:22
tags: linux, system administration

### LOCATE

Very fast way of finding a file on a system as compared to find.

caches all files within a database . updated using a cronjob on a regular basis.

    yum install mlocate

    locate httpd

if file not findable, then you may need to manually update database using:::

    updatedb

### FIND

more flexible than locate. Slower. More powerful.

find by name

    find /etc -name motd

find by user

    find / -user adm1n
    find / -uid 1004

find file modified in last 3 days

    find / -mtime -3   >>> modified in last 3 days 

search for files with a specific permission (e.g. world read-write permissions)

    find / -perm 777

execute commands using find syntax 

    find /home -user jeff -type f -exec cat {} \;

    find /home -user jeff -type f -exec cp {} /home/ \;

    find / -user jeff -type f -exec rm {} \;





























































