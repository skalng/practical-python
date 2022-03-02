'''
Created on 02.03.2022

@author: ho_ksk
__updated__='2022-03-02 23:57:28'
'''

# ticker.py - Exercise 6.10 / 6.11 / 6.12

import csv

import report
from follow import follow

portfolio = report.read_portfolio('Data/portfolio.csv')

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def make_dicts(rows, headers):
    for row in rows:
        yield {h: val for h, val in zip(headers, row)}


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def select_coloums(rows, indices):
    for row in rows: 
        yield [row[i] for i in indices]

    
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_coloums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = filter_symbols(rows, portfolio)
    return rows


def ticker(portfile: str, logfile: str, fmt: str):
    
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = csv.reader(lines)
    rows = select_coloums(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = filter_symbols(rows, portfolio)
    
    from tableformat import create_formatter
    
    formatter = create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([ v for _, v in row.items()])
    
   
    



if __name__ == '__main__':
#     lines = follow('Data/stocklog.csv')
#     rows  = parse_stock_data(lines)
#     for row in rows:
#         print(row)

    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
    





