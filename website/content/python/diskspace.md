Title: Monitoring diskspace using Python
Date: 2018-05-22 23:22
tags: monitoring, python, coding, linux, scripting
Author: Jonathan Gray

This could be done much easier in bash but the point was to practice Python.
There is also the future plan to use HTTP POST requests to send this data to
a web UI.

In retrospect I think using subprocess library and piping the output to stdout
would have been more efficent.
```python
#!/usr/bin/env python3.6

import smtplib

""" script that gets df -h output > sorts it
compares output to threshold
if output exceed threshold send alert via email
"""

define partition and threshold parameters

partition = '/home'
threshold = 85

#use smtplib to send alert mail to administrator

def send_alert_mail():
server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("emailAddress", "password")
msg = ("alert:: disk space is beyond 85% threshold")
# send alert email using parameters above
server.sendmail("FROM", "TO", msg)
server.quit()

print("""
Checking partitions for how much space is available...
""")

# opens disk_output.txt with df -h output (appended using a cronjob)
# split lines from file into a list using for loop
# acquire partition and threshold values using list indexing

with open('disk_output.txt', 'r') as f:  ### cronjob ammends df -h output to txt file. could use subprocess & stdout also
for lines in f:
split_line = lines.split()
if split_line[5] == partition:
if int(split_line[4][:-1]) >= threshold:
print(f"alert:: \t disk space in {partition} is beyond {threshold}%")
send_alert_mail()
```































































