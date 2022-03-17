'''
Created on 02.03.2022

@author: ho_ksk
__updated__='2022-03-03 10:24:41'
'''

# ticker.py - Exercise 6.10 / 6.11 / 6.12

import csv

from porty import report
from porty import tableformat
from follow import follow

portfolio = report.read_portfolio('Data/portfolio.csv')

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)
#     for row in rows:
#         yield dict(zip(headers, row))


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
    return rows


def ticker(portfile: str, logfile: str, fmt: str):
    
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
        
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([ row['name'], row['price'], row['change']])
    
   
    



if __name__ == '__main__':
#     lines = follow('Data/stocklog.csv')
#     rows  = parse_stock_data(lines)
#     for row in rows:
#         print(row)

    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
    





