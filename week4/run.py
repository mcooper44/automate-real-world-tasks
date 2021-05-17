import os
import requests
FILE_PATH = '~/supplier-data/descriptions/'

def parse_text_file(txt_f):
    fields = ['name', 'weight', 'description', 'image_name']
    field_index = 0
    structure = {}
    try:
        with open(txt_f, 'r') as text:
            for line in text:
                key = fields[field_index]
                if key == 'weight':
                    structure[key] = int(line)
                else:
                    structure[key] = line
                field_index +=1
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
    for infile in os.listdir(FILE_PATH)
        if infile.endswith('.txt'):
            data_dictionary = parse_text_file(f'{FILE_PATH}{infile}')
            file_structure.append(data_dictionary)
            report_entry = 'name: {}<br><br/>'.format(data_dictionary['name']) +
                           'weight: {}<br><br/>'.format(data_dictionary['weight']) +
                           '<br><br/>'
            report_structure += report_entry 
                # post the text descriptions to the webserver
    try:
        post_json(file_structure)
    except Exception as error:
        raise error
