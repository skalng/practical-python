# pcost.py
#
# Exercise 1.27 / 6.2 
 

from report import read_portfolio

def portfolio_cost(filename):

    portfolio = read_portfolio(filename)
    return portfolio.total_cost



if __name__ == '__main__':
    
    print(portfolio_cost('Data/portfolio.csv'))