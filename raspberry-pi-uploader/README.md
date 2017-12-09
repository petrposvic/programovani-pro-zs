# Raspberry Pi 3 Uploader

Set of scripts enabling my students upload Python 3 code to Raspberry Pi 3 and run it.

# /etc/rc.local

/usr/bin/screen -d -m /home/pi/krouzek-zs-volyne/autostart.sh

After boot sends "ip a" output to my e-mail so I know Raspberry Pi's network address. Then starts simple webserver on
localhost (but accessible from network) on port 3000.

# Webserver

Listening on 0.0.0.0:3000. Enable post Python 3 code and run it.
