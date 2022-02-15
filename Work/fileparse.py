# fileparse.py
#
# Exercise 3.3

import csv
from typing import List

def parse_csv(filename: str, 
              select=[], 
              types=[], 
              has_headers=True, 
              delimiter=',', 
              silence_errors=True) -> List[dict]:
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows    = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else None
        select  = select if select else headers
        records = []
        for i, row in enumerate(rows, 1):
            try:
                if row == []:
                    raise ValueError
                if has_headers:
                    record = { h: val for h, val in (zip(headers, row)) if h in select }
                    converted = { k: func(v) 
                                for func, k, v 
                                in zip(types, record.keys(), record.values())} if types else record
                    records.append(converted)
                else:
#                    record    = tuple(row)
                    converted = [func(val) for func, val in zip(types, row)] if types else row
                records.append(tuple(converted))
            except ValueError:
                if not silence_errors:
                    print(f'Bad row: "{row}" at line {i}')

    return records
                    



