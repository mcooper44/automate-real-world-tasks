#!/usr/bin/python3.8

import os
from PIL import Image

PRODUCTION_PATH = 'supplier-data/images/'
TESTING_PATH = 'test_images/'
PATH = TESTING_PATH

def open_and_process_image(the_image, source_p, conv_type='RGB',
                           new_size=(600,400), new_format='JPEG',
                           new_ext = '.jpeg',
                           save_loc='test_images/'):

    '''
    opens an image file and returns it
    resized in a new format to the location specified
    at save_loc
    the_image: should be a file name and should not include path
    source_p: is the path where the file is located
    conv_type: is the colour model that will be used RGB, RGBA etc
    new_size: tuple of the new image dimensions
    new_format: format that image will be convereted to
    new_ext: is the extension that will be added to the file name in place of
    the old one
    save_loc: location the new image file will be saved at
    

    '''

    if not the_image.endswith(new_ext):
        # swap extensions on the file 
        new_n = os.path.splitext(the_image)[0] + new_ext
        # build the new path to save the file
        out_file = f'{save_loc}{new_n}'
        try:
            with Image.open(f'{source_p}{the_image}') as m:
                m.convert(conv_type).resize(new_size).save(out_file, new_format)
        except OSError as e1:
            print(f'cannot process or save {the_image}')
            print(f'due to: {e1}')
        except Exception as oe:
            print(f'{the_image} raised {oe}')
    print(f'converted {the_image} to {new_size} size + {new_format}')

if __name__ == '__main__':
    for infile in os.listdir(PATH):
        open_and_process_image(infile, PATH)
