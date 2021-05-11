#!/usr/bin/python3.8

import sys, os
from PIL import Image

RESIZE_TARGET = (128,128)
FORMAT_TARGET = 'JPEG'
OUT_BIN = 'output/'

def open_and_process_image(the_image, source_p):
    '''
    opens a file name of an image and returns it
    resized, rotated and in jpeg format
    '''
    new_n = os.path.splitext(the_image)[0] + '.jpg'
    outfile = f'{OUT_BIN}{new_n}'
    try:
        with Image.open(f'{source_p}{the_image}') as m:
            m.transpose(Image.ROTATE_270).resize(RESIZE_TARGET).convert('RGB').save(outfile, FORMAT_TARGET)
            print(f'wrote: {outfile}')
    except OSError as e1:
        print(f'cannot process {the_image}')
        print(e1)
    except Exception as oe:
        print(f'{the_image} raised {oe}')

if __name__ == '__main__':
    for infile in os.listdir('images/'):
        open_and_process_image(infile, 'images/')
