#!/usr/bin/python3.8

from collections import defaultdict
import operator

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from re import sub
from decimal import Decimal
import sys

sample_ds = [
            {
            "id": 47,
            "car": {
                                "car_make": "Lamborghini",
                                "car_model": "Murciélago",
                                "car_year": 2002
                        },
            "price": "$13724.05",
            "total_sales": 149
            },
            {
                "id": 34,
                "car": {
                                    "car_make": "T-34",
                                    "car_model": "Model 85",
                                    "car_year": 1934
                            },
                "price": "$5000",
                "total_sales": 1917
            },
            {
                "id": 20,
                "car": {
                                    "car_make": "T-28",
                                    "car_model": "Kirov",
                                    "car_year": 1932
                            },
                "price": "$1724.05",
                "total_sales": 20
            }

            ]


def summarize(struct):
    headers = ['ID', 'Car', 'Price', 'Total Sales']
    summary = []
    for item in struct:
        ID = item['id']
        vehicle = '{} {} ({})'.format(item['car']['car_make'],
                                      item['car']['car_model'],
                                      item['car']['car_year'])
        amount = item['total_sales']
        price = item['price']
        price_value = Decimal(sub(r'[^\d.]', '', price))
        sales = '${:,.2f}'.format(amount * price_value)
        summary.append([ID, vehicle, price, amount])
    sorted_sum = sorted(summary, key=operator.itemgetter(3))
    sorted_sum.insert(0, headers)
    return sorted_sum

def most_sales(struct):
    model = None
    sales = 0
    for item in struct:
        if item['total_sales'] > sales:
            sales = item['total_sales']
            model = item['car']['car_model']
    return 'The {} had the most sales: {}'.format(model, sales)

def best_year(struct):
    year_struct = defaultdict(int)
    for item in struct:
        year = item['car']['car_year']
        year_struct[year] += item['total_sales']
    best_year = max(year_struct.items(), key=operator.itemgetter(1))[0]
    return 'The most popular year was {} with {} sales'.format(best_year,
                                                               year_struct[best_year])

def generate(filename, title, additional_info, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    table_style = [("GRID", (0,0), (-1,-1), 1, colors.black),
                  ('FONTNAME', (0,0),(-1,0), 'Helvetica-Bold'),
                  ('ALIGN', (0,0), (-1,-1), 'CENTRE')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line=Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line,
                  report_table])

def main():
    info = '{}<br/>{}<br/>'.format(most_sales(sample_ds),best_year(sample_ds))
    tab = summarize(sample_ds)
    generate('test.pdf', 'Vehicle Sales',info, tab) 

main()
