#!/usr/bin/python3.8

import shutil
import psutil
import requests
import socket
import time

import emails


SENDER = 'automation@example.com'
RECIPIENT = 'username@example.com' # this will need to get changed
BODY = 'Please check your system and resolve the issue as soon as possible.'

def check_connectivity():
    ''' attempts to resolve google and checks if
    the status code is 200 '''
    response = requests.get('https://www.google.com')
    sc = response.status_code == 200
    return {'result': response.status_code,
            'str': f'Can connect to internet: {sc}',
            'alert': sc != True,
            'subject': 'Error - cannot connect to internet.'}

def check_localhost(host_ip='127.0.0.1', host_name='localhost'):
    '''attempts to resolve a host
    default checks local host'''
    lh = socket.gethostbyname(host_name)
    connection = (lh == host_ip)
    return{'result': lh,
           'str': f'can connect to local host {host_name}: {connection}',
           'alert': connection != True,
           'subject': 'Error - localhost cannot be resolved to 127.0.0.1'} 

def get_du(threshold=20):
    '''returns % of disk free'''
    du = shutil.disk_usage('/')
    dpc = du.free/du.total*100
    threshold_passed = dpc >= threshold
    return {'result': dpc,
            'str': f'Disk used is: {du.free/1048576}MB\nTotal % of disk free is: {dpc}',
            'alert': threshold_passed == False,
            'subject': 'Error - Available disk space is less than 20%'}

def get_memory(threshold=500):
    '''amount of memory free in MB'''
    vm = psutil.virtual_memory()
    free_mb = vm.free/1048576
    return {'result': free_mb,
            'str': f'% of memory used: {vm.percent}\nMB free is: {vm.free:.2f}',
            'alert': free_mb<500,
            'subject': 'Error - Available memory is less than 500MB'}

def get_cpu(duration=2):
    '''returns cpu % free'''
    usage = psutil.cpu_percent(duration)
    return {'result': usage,
            'str': f'cpu usage over {duration} seconds is {usage}',
            'alert': usage > 80,
            'subject': 'Error - CPU usage is over 80%'}

def email_alert(alert_subject):
    '''accepts an alert subject and using the hard coded values
    sends an alert email '''
    alert_message = emails.generate_email(SENDER, RECIPIENT, 
                                          alert_subject, BODY,
                                          attachment_path=None)
    emails.send_email(alert_message)

if __name__ == '__main__':
    tests = [check_connectivity, check_localhost, get_du, get_memory, get_cpu]
    for test in tests:
        outcome = test()
        print(outcome['str'])

        if outcome['alert']:
            print(outcome['subject'])
            # UNCOMMENT THIS WHEN IT'S TIME TO GO LIVE
            #email_alert(outcome['subject'])
