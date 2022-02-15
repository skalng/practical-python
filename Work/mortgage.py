# mortgage.py
#
# Exercise 1.7

principal  = 500000.0
rate       = 0.05
payment    = 2684.11
total_paid = 0.0
extra_payment = 1000
month = 0

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if month <= 12:
        principal  = principal - extra_payment
        total_paid = total_paid + extra_payment

print('Total paid', round(total_paid, 2), 'total number of month', month)
