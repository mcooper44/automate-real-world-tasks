import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


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

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    title = 'Processed Update on {}'.format(
                datetime.today().strftime('%Y-%m-%d'))
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line=Spacer(1,20)
    report.build([report_title, empty_line, report_info])



if __name__ == '__main__':
    report_structure = ''
    # parse the text files and build a json structure of descriptions
    for infile in os.listdir(FILE_PATH)
        if infile.endswith('.txt'):
            data_dictionary = parse_text_file(f'{FILE_PATH}{infile}')
            report_entry = 'name: {}<br><br/>'.format(data_dictionary['name']) +
                           'weight: {}<br><br/>'.format(data_dictionary['weight']) +
                           '<br><br/>'
            report_structure += report_entry 
                # post the text descriptions to the webserver
