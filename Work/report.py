# report.py
#
# Exercise 2.4

import csv
from typing import List, Iterable

def read_csv_data(file: str) -> List[str]:
    with open(file) as f:
        lines = f.readlines()
    return lines


def read_portfolio(lines: List[str]) -> List[dict]:
    portfolio = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        try:
            holding = {headers[0]: row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
            portfolio.append(holding)                
        except ValueError:
            print('Bad row:', row)
    return portfolio


def read_prices(lines: List[str]) -> dict:
    prices = {}
    rows = csv.reader(lines)
    for line_num, row in enumerate(rows, start=1):
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            print(f'Bad row at line {line_num}:', row)
    return prices


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
    portfolio_port = read_csv_data(portfolio_fn)
    prices_port    = read_csv_data(prices_fn)
    
    portfolio = read_portfolio(portfolio_port)
    prices    = read_prices(prices_port)
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
    
    
    
    
    
