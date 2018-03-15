# -*- coding: utf-8 -*-
"""
@author: LN

print the lowest fixed monthly payment that should pay off in a year 

 Test Case: 
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
"""
fixedPay = 10
balance = 3329
annualInterestRate = 0.2
monthlyRate = (annualInterestRate) / 12.0
while True: 
    updatedBal = balance
    for each in range (0, 12):
        monthlyUnpaid = updatedBal - fixedPay
        updatedBal = monthlyUnpaid * (monthlyRate + 1)
    if updatedBal > 0:
        fixedPay += 10
    else:
        break
print (str(fixedPay))