#!/usr/bin/python3.8

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path=None):
    '''generate a message object and return it.
    if attachment_path - add a file to the message'''
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetype.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        
        with open(attachement_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)
    return message

def send_email(message):
    '''take a message object returned from generate_email function
    and send it out'''
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
    print('message sent')
