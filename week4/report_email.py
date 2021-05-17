#!/usr/bin/python3.8
import emails


if __name__ == '__main__':
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed' +
    ' list is attached to this email'
    attachment = '~/supplier-data/descriptions'
    the_mail = emails.generate_email(sender, recipient, subject, body,
                                     attachment)
    send_email(the_mail)
