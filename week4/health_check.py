#!/usr/bin/python3.8

import shutil
import psutil
import requests
import socket

def check_connectivity():
    response = requests.get('https://www.google.com')
    sc = response.status_code == 200
    return {'result': response.status_code,
            'str': f'Can connect to internet: {sc}',
            'alert': sc != True,
            'subject': None}

def check_localhost(hostname='127.0.0.1'):
    lh = socket.gethostbyname('localhost')
    connection = (lh == hostname)
    return{'result': lh,
           'str': f'can connect to local host {hostname}: {connection}',
           'alert': connection != True,
           'subject': None} 

def get_du(threshold=20):
    '''returns % of disk free'''
    du = shutil.disk_usage('/')
    dpc = du.free/du.total*100
    threshold_passed = dpc >= threshold
    return {'result': dpc,
            'str': f'Disk used is: {du.free/1048576}MB\nTotal % of disk free is: {dpc}',
            'alert': threshold_passed,
            'subject': None}

def get_memory(threshold=500):
    '''amount of memory free in MB'''
    vm = psutil.virtual_memory()
    free_mb = vm.free/1048576
    return {'result': free_mb,
            'str': f'% of memory used: {vm.percent}\nMB free is: {vm.free:.2f}',
            'alert': free_mb<500,
            'subject': None}

def get_cpu(duration=2):
    '''returns cpu % free'''
    usage = psutil.cpu_percent(duration)
    return {'result': usage,
            'str': f'cpu usage over {duration} seconds is {usage}',
            'alert': usage > 80,
            'subject' None}




if __name__ == '__main__':
    tests = [check_connectivity, check_localhost, get_du, get_memory, get_cpu]
    for test in tests:
        outcome = test()
        print(outcome['str'])
        

