# Find out how long to pay off a loan

principal_amount = 300000
payment = 2189
rate = .0287
total_paid = 0

while principal_amount > 0:
    interest = principal_amount*(rate/12)
    principal_amount = principal_amount + interest - payment
    total_paid = total_paid +payment

print('Total paid:', total_paid)