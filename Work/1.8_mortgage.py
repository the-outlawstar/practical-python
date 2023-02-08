# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = .05
payment = 2684.11
total_paid = 0.0
extra_payments = [1000]*12
month_counter = 0

while principal > 0:
    if len(extra_payments) != 0:
        principal = principal * (1 + rate / 12) - payment - extra_payments[0]
        total_paid = total_paid + payment + extra_payments[0]
        extra_payments.pop()
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    month_counter += 1

print(f'Total paid {total_paid:.2f}\nMonths until paid off {month_counter}')