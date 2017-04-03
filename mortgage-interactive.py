import sys

# Find out how long to pay off a loan

principal_amount = 300000
payment = 2189
rate = .0287
total_paid = 0
month = 0
"""
# extra payment info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month =60
month = 0
"""

out = open('schedule.txt','w')

print('{:>5s} {:>10s} {:>s} {:>10s}'.format('Month','Interest','Principal','Reminaing'),file=out)
while principal_amount > 0:
    month += 1
    """
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    """
    interest = principal_amount*(rate/12)
    principal_amount = principal_amount + interest - payment
    total_paid = total_paid + payment

    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month,interest,payment-interest,principal_amount),file=out)
out.close()
print('Total paid:', total_paid)