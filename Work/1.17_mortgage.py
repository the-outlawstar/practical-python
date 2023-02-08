# mortgage.py
#
# Exercise 1.17
principal = 500000.0
rate = .05
payment = 2684.11
total_paid = 0.0
extra_payment = int(input('Please enter the extra payment ammount: ') or '1000')
extra_payment_start_mo = int(input('Please enter the extra payment start month: ') or '61')
extra_payment_end_mo = int(input('Please enter the extra payment end month: ') or '108')
month_counter = 0

while principal > 0:
    if principal - payment <= 0:
        payment = payment - abs(principal)
        principal -= payment
        total_paid += payment
        break
    elif extra_payment_start_mo <= month_counter <= extra_payment_end_mo:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    month_counter += 1
    print(f'{month_counter:4.0f} {total_paid:10.2f} {principal:10.2f}')
    
print(f'Total paid {total_paid:.2f}\nMonths {month_counter}')