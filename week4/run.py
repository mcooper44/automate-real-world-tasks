#!/usr/bin/python3.8
import os
import requests
PRODUCTION_PATH = '~/supplier-data/descriptions/'
FILE_PATH = 'test_files/'

def parse_text_file(txt_f):
    fields = ['name', 'weight', 'description', 'image_name']
    field_index = 0
    structure = {}
    f_root = txt_f.split('/')[-1].split('.')[0]
    try:
        with open(txt_f, 'r') as text:
            for line in text:
                key = fields[field_index]
                if key == 'weight':
                    structure[key] = int(line)
                else:
                    structure[key] = line.rstrip()
                field_index +=1
            structure['image_name'] = '{}.jpg'.format(f_root)
            return structure
    except Exception as error:
        print(f'{txt_f} raised {error}')

def post_json(json_struct):
    try:
        attempt.post(URL, data=json.dumps(json_struct))
        attempt.raise_for_status()
    except HTTPError as http_error:
        print(f'HTTP error was raised: {http_err}')
        print(f'using {file_path} and {url}')
    except Exception as other_error:
        print(f'ERROR: {other_error}')
    else:
        print(f'description uploaded')


if __name__ == '__main__':
    file_structure = []
    # parse the text files and build a json structure of descriptions
    for infile in os.listdir(FILE_PATH):
        if infile.endswith('.txt'):
            data_dictionary = parse_text_file(f'{FILE_PATH}{infile}')
            file_structure.append(data_dictionary)

    # post the text descriptions to the webserver
    try:
        print(file_structure)
        #post_json(file_structure)
    except Exception as error:
        raise error
