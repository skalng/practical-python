# report.py
#
# Exercise 2.4

import csv
from typing import List, Iterable

import fileparse



def read_portfolio(filename: str) -> List[dict]:
    with open(filename) as f:
        lines = f.readlines()
        
    portfoliodict = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
        
    return portfoliodict


def read_prices(filename: str) -> dict:
    with open(filename) as f:
        lines = f.readlines()
    
    return {x[0]: x[1] for x in fileparse.parse_csv(lines, types=[str, float], has_headers=False)}



def print_report(report: Iterable[list]) -> None:
    '''
    Print out the portfolio report as a table:
              Name     Shares      Price     Change
        ---------- ---------- ---------- ---------- 
                AA        100       32.2     -22.98
               IBM         50       91.1      15.18
               CAT        150      83.44     -47.98
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10s %10s %10s'  % row)


def portfolio_report(portfolio_fn: str, prices_fn: str) -> None:
    '''
    Generates a portfolio report from a portfolio- and prices-file and print it 
    out as a table using print_report
    '''
    
    portfolio = read_portfolio(portfolio_fn)
    prices    = read_prices(prices_fn)
    # --- Make a list of (name, shares, price, change) tuples 
    report = [(h['name'], 
               h['shares'], 
               h['price'], 
               round(prices[h['name']]-h['price'], 2)) 
            for h in portfolio]
    print_report(report)

def main():
    portfolio_fn = 'Data/portfolio.csv'
    prices_fn    = 'Data/prices.csv'

    portfolio_report(portfolio_fn, prices_fn)
    

if __name__ == "__main__":
    main()
    
    
    
    
    
