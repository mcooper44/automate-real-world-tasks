#!/usr/bin/python3.8

import os
import requests
import json

TARGET_DIR = 'reviews/'
STRUCTURE = ['title', 'name', 'date', 'feedback']


def parse_text_files(txt_path):
    DICT_STRUCT = []
    for txt_f in os.listdir(txt_path):
        f_p = os.path.join(txt_path, txt_f)
        if os.path.isfile(f_p) and txt_f.endswith('.txt'):
            DICT = {}
            with open(f_p, 'r', encoding='utf-8') as txt:
                index = 0
                for line in txt:
                    key = STRUCTURE[index]
                    DICT[key] = line.rstrip()
                    index += 1
            DICT_STRUCT.append(DICT)
        else:
            continue
    #return json.dumps(DICT_STRUCT)
    return DICT_STRUCT

def post_review(url, dct):
    if url == 'url':
        return 201
    else:
        attempt = requests.post(url, data=dct)
        return attempt.status_code


if __name__ == '__main__':
    j_txt = parse_text_files(TARGET_DIR)
    for dct in j_txt:
        status = post_review('url', dct)
        if status == 201:
            print('yes')
        else:
            print('no')
