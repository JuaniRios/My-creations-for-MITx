# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:35:24 2019

@author: juani
"""
balance = 0
currentBalance = balance
annualInterestRate = 0
monthlyPaymentRate = 0

monthRate = annualInterestRate/12

paymentMonthly = {}
balanceMonthly = {}

def interestBalance():
    return monthRate*currentBalance
def payMonth():
    return monthlyPaymentRate*currentBalance
def updateBalance():
    global currentBalance
    currentBalance-=payMonth()
    currentBalance+=interestBalance()
    return currentBalance

def startCalculation(n):
    #n being number of months trying to calculate
    for i in range(1, n+1):
        paymentMonthly['month{0}'.format(i)] = payMonth()
        balanceMonthly['month{0}'.format(i)] = updateBalance()
        if i == 12:
            print('Remaining balance: ' + str(round(balanceMonthly['month{0}'.format(i)], 2)))

startCalculation(12)