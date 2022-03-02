'''
Created on 02.03.2022

@author: ho_ksk
__updated__='2022-03-02 14:45:00'
'''

# ticker.py - Exercise 6.10


from follow import follow
import csv
from _testbuffer import slice_indices


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
    return rows



if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows  = parse_stock_data(lines)
    for row in rows:
        print(row)







