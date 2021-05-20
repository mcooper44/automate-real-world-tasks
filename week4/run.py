#!/usr/bin/python3.8
import os
import requests

PRODUCTION_PATH = 'supplier-data/descriptions/'
FILE_PATH = 'test_files/'
URL = 'http://localhost/fruits/' # replace localhost with IP

def parse_text_file(txt_f):
    '''opens a text file and creates a dictionary
    that can POSTed to an end point'''
    fields = ['name', 'weight', 'description', 'image_name']
    field_index = 0
    structure = {}
    f_root = txt_f.split('/')[-1].split('.')[0]
    try:
        with open(txt_f, 'r') as text:
            for txt in text:
                line = txt.rstrip()
                key = fields[field_index]
                if key == 'weight':
                    no_lbs = line.strip(' lbs')
                    structure[key] = int(no_lbs)
                else:
                    structure[key] = line.rstrip()
                field_index +=1
            structure['image_name'] = '{}.jpeg'.format(f_root)
            return structure
    except Exception as error:
        print(error)

def post_json(URL, json_struct):
    '''posts a dictionary/json to a URL'''
    try:
        r = requests.post(URL, json=json_struct)
        r.raise_for_status()
    except Exception as error:
        print(error)

if __name__ == '__main__':
    # parse the text files and build a json structure of descriptions
    for infile in os.listdir(FILE_PATH):
        if infile.endswith('.txt'):
            data_dictionary = parse_text_file(f'{FILE_PATH}{infile}')
            post_json(URL, data_dictionary)
