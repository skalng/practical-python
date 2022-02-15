# report.py
#
# Exercise 2.4

import csv
from typing import List, Iterable

def read_portfolio(filename: str) -> List[dict]:
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
                portfolio.append(holding)                
            except ValueError:
                print('Bad row:', row)

    return portfolio

def read_prices(filename: str) -> dict:
    prices = {}
#    line_num = 0
    with open(filename) as f:
        rows = csv.reader(f)
        for line_num, row in enumerate(rows, start=1):
#            line_num += 1
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Bad row at line {line_num}:', row)
    return prices

def portfolio_report(portfolio_fn: str, prices_fn: str) -> List[list]:
    '''
    Generates a portfolio report from a portfolio- and prices-file
    '''
    portfolio = read_portfolio(portfolio_fn)
    prices    = read_prices(prices_fn)
    report = [(h['name'], 
               h['shares'], 
               h['price'], 
               round(prices[h['name']]-h['price'], 2)) 
            for h in portfolio]
    return report


def print_report(report: Iterable[list]) -> None:
    '''
    Print out the portfolio report as a table of 
    'Name', 'Shares', 'Price', 'Change'
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10s %10s %10s'  % row)




