Title: SELinux contexts
Date: 2018-05-21 23:22
tags: SELinux, Red Hat, Linux, Security
Author: Jonathan Gray

## SELinux contexts - what to look for 

SELINUX RESTORE, ADD, DELETE CONTEXTS


### RESTORING CONTEXTS

	- Could use autorelabel
	- touch /.autorelabel
	- /.autorelabel
	- On next reboot it will relabel everything based on
	proper context

or use **restorecon** command.

### CONTEXTS CONTROLLED BY	

semanage fcontext -l 

	- Reccomended to use context as defined in semanage fcontext ONLY
	- NOT set them manually.
	- You can use restorecon to restore context based on defaults 

### ADDING CONTEXT TO DIRECTORY 

let us say you set apache DocumentRoot and DirectoryIndex to /content instead of /var/www

    [root@j0nn91 content]# ls -Z
    -rw-r--r--. root root unconfined_u:object_r:default_t:s0 index.html

Problem is index.html does not have httpd context, so httpd service will not have access to the file.
Therefore page will be "permission denied" **REGARDLESS OF PERMISSIONS**.

so you need to set the semanage context for this directory to reflect /var/www:::

    /var/www(/.*)?      all files          system_u:object_r:httpd_sys_content_t:s0


### COMMAND TO ADD CONTEXT TO DIRECTORY

    semanage fcontext -l | grep /var/www --> can take context and also (/.*) if you forget

    semanage fcontext -a -t httpd_sys_content '/content(/.*)?'
 
    [root@j0nn91 content]# semanage fcontext -a -t httpd_sys_content_t '/content(/.*)?'

    [root@j0nn91 content]# ls -Z
    -rw-r--r--. root root unconfined_u:object_r:default_t:s0 index.html

But file is still default_t. Need to do restorecon to restore to semanage defaults.

### RESTORECON TO SET CONTEXT BACK TO DEFAULTS 

    restorecon -Rv /content

### TO DELETE NEWLY SET CONTEXT 

    [root@j0nn91 content]# semanage fcontext -l | grep /content
    /content(/.*)?                                     all files          system_u:object_r:httpd_sys_content_t:s0


    [root@j0nn91 content]# semanage fcontext -d "/content(/.*)?"


The biggest thing to know with SELinux when you are troubleshooting is improper context
and incorrect labelling of files can be the main culprits.


