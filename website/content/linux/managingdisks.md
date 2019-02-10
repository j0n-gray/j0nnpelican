Title: A concise primer on filesystems & block devices
Date: 2018-06-28 
tags: linux, system administration

### lsblk

hard drives are a type of block device in unix systems. they usually follow the format of /dev/sdx 

checking all physical hdds and partitions available [ useful because it picks up unmounted hdds too]

	NAME                     MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
	sda                        8:0    0 238.5G  0 disk
	sda1                       8:1    0  19.5G  0 part
	md1                        9:1    0  19.5G  0 raid1 /
	sda2                       8:2    0 218.5G  0 part
	md2                        9:2    0 218.4G  0 raid1 /home

###blkid

you want to get blkid of a device, because mounting by UUID is safer than by using the direct device path.
the device path can change, the UUID cannot.  

	/dev/loop0: UUID="231ecc49-7c0a-4272-bf67-36dc110c711f" TYPE="xfs"
	/dev/sda1: UUID="8e3cb146-0db2-9380-a4d2-adc226fd5302" TYPE="linux_raid_member" PARTUUID="d5bfc4bd-01"


### /etc/fstab

sudo vim /etc/fstab. example entry below

	UUID=231ecc49-7c0a-4272-bf67-36dc110c711f /mnt/disk        ext4    defaults        0 0


you can mount everything in /etc/fstab with mount -a. this also tests if the /etc/fstab entry you created actually works.


use mount | grep "disk" to check if the disk is mounted.

or just mount | less 


### tune2fs

really useful for when you mount a large external storage disk 

a lot of linux distros reserve 5% of space for new partitions for root user & system services. this in theory means even when you
run out of disk space you can still login as the root user and make necessary changes to recover disk space.

this is not relevant for a disk that isnt mounted to the root FS, 5% can be a significant amount of space for larger disks. e.g. about 50gb for
1TB. so we can free up this space.

	tune2fs -m 0 /dev/sda1 


also
	tune2fs -l /dev/sda1 

to view all specific disk information specifically::

	sudo tune2fs -l /dev/md1 | grep "Reserved"
	Reserved block count:     255986
	Reserved GDT blocks:      1022
	Reserved blocks uid:      0 (user root)
	Reserved blocks gid:      0 (group root)




























































