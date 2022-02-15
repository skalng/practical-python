# pcost.py
#
# Exercise 1.27
 
import sys
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            try:
                h = dict(zip(headers, row))
                total_cost += int(h['shares']) * float(h['price'])
            except ValueError:
                print(f'Bad row at {rowno}:', row)

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
