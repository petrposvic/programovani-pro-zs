#!/usr/bin/python3

import smtplib
import subprocess

sender = 'petr@posvic.cz'
receivers = ['petr@posvic.cz']

message = """From: Raspberry Pi 3 <petr@posvic.cz>
To: Petr Posvic <petr@posvic.cz>
Subject: Raspberry Pi started

Assigned IP address is:
{}
""".format(subprocess.getoutput('ip a'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('petr@posvic.cz', 'password')
    server.sendmail(sender, receivers, message)
    print('Successfully sent email')
except SMTPException:
    print('Error: unable to send email')

