# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:52:49 2018

@author: LN


# Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01 
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38
  """
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = (annualInterestRate) / 12.0

for each in range (0, 12):
    minMonthlyPay = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPay
    
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance) 
      
print (str(round(balance, 2)))