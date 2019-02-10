Title: SystemD Timer Units > Cron 
Date: 2018-10-21 14:00
tags: linux, automation

Using a SystemD service with timers is a great alternative to Cron. 

This command is useful to have visibility over all units :

```
systemctl list-units

```

Let's create a unit. First, we need a service
 

```
vim /etc/systemd/system/RunMyScript.service

```

You are saying create a unit, which is a service, the
service runs a script and that you wish to run it
after multi-user.target. Multi-user target is the equivalent
to run level 3 which is a non-graphical multi user system.
This is what your system will be (at least) in most cases.

```
[Unit]

Description= some Python script that does something
After=multi-user.target

[Service]
ExecStart= /usr/bin/python /usr/local/bin/somescript.py

[Install]
WantedBy=multi-user.target


```

Save then

```
chmod 664 /etc/systemd/system/RunMyScript.service

```

Reload SystemD:

```

systemctl daemon-reload

```

Then you can start the service with

```
systemctl start RunMyScript.service

```

Now create the timer

``` 
vi /etc/systemd/system/RunMyScript.timer

```

Then paste the following


```
[Unit]
Description=Run my script at midnight every day

[Timer]
OnCalendar=*-*-* 00:00:00
Unit=RunMyScript.timer

[Install]
WantedBy=multi-user.target

```

This time you need to enable it at boot, then start the timer.

```
systemctl enable RunMyScript.timer

```

Then start it

```
systemctl start backup.timer

```


If you make any changes to the timer you need to run


```
systemctl daemon-reload

```

But back to the original question: why use SystemD timers? Firstly, SystemD timers can be accurate to the unit
of miliseconds or even further should you want such accuracy. Secondly, since its now a systemd service managed
by a timer, you can very easily manage it with the normal systemctl commands.


This also means you have logging for free! Simply run journalctl command to check the unit. You can also see 
similar output (but less verbose) in systemctl status RunMyScript.

```
journalctl -xb -u RunMyScript

```


### Conclusion:::

SystemD units are good to use when applicable.


### sources / further reading:

1. [Digital Ocean Guide On SystemD units](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)
2. [SystemD manpage](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
3. [Arch Linux Wiki On SystemD](https://wiki.archlinux.org/index.php/systemd)
























































