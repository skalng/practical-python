# report.py
#
# Exercise 2.4

import csv
from typing import List, Iterable

import fileparse
from stock import Stock
from tableformat import create_formatter, TableFormatter, TextTableFormatter, CSVTableFormatter, HTMLTableFormatter



def read_portfolio(filename: str) -> List[Stock]:
    with open(filename) as f:
        lines = f.readlines()
        
    portfoliodict = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    return [ Stock(d['name'], d['shares'], d['price']) for d in portfoliodict]
        


def read_prices(filename: str) -> dict:
    with open(filename) as f:
        lines = f.readlines()
    
    return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    return [(s.name, 
               s.shares, 
               s.price, 
               round(prices[s.name] - s.price, 2)) 
            for s in portfolio]
    


def print_report(reportdata: Iterable[list], formatter: TableFormatter) -> None:
    '''
    Print out the portfolio report as a table:
              Name     Shares      Price     Change
        ---------- ---------- ---------- ---------- 
                AA        100       32.2     -22.98
               IBM         50       91.1      15.18
               CAT        150      83.44     -47.98
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, shares, price, change]
        formatter.row(rowdata)


def portfolio_report(portfolio_fn: str, prices_fn: str, fmt='txt') -> None:
    '''
    Generates a portfolio report from a portfolio- and prices-file and print it 
    out as a table using print_report
    '''
    
    portfolio = read_portfolio(portfolio_fn)
    prices    = read_prices(prices_fn)
    # --- Make a list of (name, shares, price, change) tuples 
    report = make_report_data(portfolio, prices)
    # --- print report
    formatter = create_formatter(fmt)
    print_report(report, formatter)

def main():
    portfolio_fn = 'Data/portfolio.csv'
    prices_fn    = 'Data/prices.csv'

    portfolio_report(portfolio_fn, prices_fn)
    

if __name__ == "__main__":
    main()
    
    
    
    
    
