# fileparse.py
#
# Exercise 3.3

import csv
from typing import List

def parse_csv(lines: List[str], 
              select=None, 
              types=None, 
              has_headers=True, 
              delimiter=',', 
              silence_errors=True) -> List[dict]:
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    rows    = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else None
    select  = select if select else headers
    # --- adapt headers to select if has_headers
    headers = [h for h in headers if h in select] if has_headers else None
    records = []
    for rowno, row in enumerate(rows, 1):
        try:
            if row == []:
                continue
            # --- convert row if types
            row = [func(val) for func, val in zip(types, row)] if types else row
            
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
            
        except ValueError:
            if not silence_errors:
                print(f'Bad row: "{row}" at line {rowno}')

    return records
                    

if __name__ == "__main__":
    lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
    port = parse_csv(lines, select=['name', 'shares', 'price'], types=[str,int,float])
    print(port)
    
    import fileparse
    with open('Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'])
    
    print('\n', portdicts)
