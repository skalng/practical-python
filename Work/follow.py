'''
Created on 01.03.2022

@author: ho_ksk
__updated__='2022-03-02 11:21:00'
'''


# follow.py

import os
import time
from report import read_portfolio
from mailcap import subst

# f = open('Data/stocklog.csv')
# f.seek(0, os.SEEK_END)
# 
# while True:
#     line = f.readline()
#     if line == '':
#         time.sleep(0.1)
#         continue
#     fields = line.split(',')
#     name   = fields[0].strip('"')
#     price  = float(fields[1])
#     change = float(fields[4])
#     if change < 0:
#         print(f'{name:>10s}{price:>10f}{change:>10f}')

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line   


def fielematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line



if __name__ == '__main__':
#     import report
#     
#     portfolio = report.read_portfolio('Data/portfolio.csv')
#     
#     
#     for line in follow('Data/stocklog.csv'):
#         fields = line.split(',')
#         name   = fields[0].strip('"')
#         price  = float(fields[1])
#         change = float(fields[4])
#         if name in portfolio:
#             print(f'{name:>10s}{price:>10.2f}{change:>10.2f}')


    ''' --- Exercise 6.8 --- '''
#     lines = follow('Data/stocklog.csv')
#     ibm = fielematch(lines, 'IBM')
#     for line in ibm:
#         print(line)
    
    
    
    ''' --- Exercise 6.9 --- '''
    import csv
    
    lines = follow('Data/stocklog.csv')
    rows = csv.reader(lines)
    for row in rows:
        print(row)
    
   
   
   
   
   
   
   
    
    