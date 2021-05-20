#!/usr/bin/python3.8

import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from run import parse_text_file

PRODUCTION_PATH = 'supplier-data/descriptions/'
FILE_PATH = 'test_files/'

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)

    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line=Spacer(1,20)
    report.build([report_title, empty_line, report_info])

if __name__ == '__main__':
    report_structure = ''
    # parse the text files and build a json structure of descriptions
    for infile in os.listdir(FILE_PATH):
        if infile.endswith('.txt'):
            data_dictionary = parse_text_file(f'{FILE_PATH}{infile}')
            report_entry = 'name: {}<br/>weight: {}<br/><br/>'.format(
                data_dictionary['name'], 
                data_dictionary['weight'])
            report_structure += report_entry 
    
    title = 'Processed Update on {}'.format(
                datetime.today().strftime('%Y-%m-%d'))
    generate_report('{}report.pdf'.format(FILE_PATH), title, report_structure)
