#!/usr/bin/python3.8
import requests
import os

URL = 'http://localhost/upload/'
PATH = 'supplier-data/images/'


def upload_file(file_path, url):
    count = 0 # track how many files go through without error
    try:

        with open(file_path, 'rb') as open_file:
            r = requests.post(url, files={'file': open_file})
            r.raise_for_status()
            count +=1
    except HTTPError as http_err:
        print(f'HTTP error was raised: {http_err}')
        print(f'using {file_path} and {url}')
    except Exception as other_error:
        print(f'ERROR: {other_error}')
    else:
        print(f'{count} files uploaded')

if __name__ == '__main__':
    for infile in os.listdir(PATH):
        if infile.endswith('.jpeg'):
            upload_file(f'{PATH}{infile}', URL)
