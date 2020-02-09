#!/usr/bin/env python3

balance, annualInterestRate, monthlyPaymentRate = 484, 0.2, 0.04

monthNum = 0
amountPaid = 0

def calcRemainingBalance(balance, annualInterestRate, monthlyPaymentRate, monthNum, amountPaid):
    #print('monthNum: {0}\tbalance: {1}\tannualInterestRate: {2}\tmonthlyPaymentRate: {3}\tmonthNum: {4}\tamountPaid: {5}'.format(monthNum, balance, annualInterestRate, monthlyPaymentRate, monthNum, amountPaid))
    if monthNum == 12:
        return balance
    else:
        monthlyInterestRate = annualInterestRate / 12.0
        minMonthlyPayment = round(monthlyPaymentRate * balance, 2)
        monthlyUnpaidBalance = balance - minMonthlyPayment
        updatedBalance = round(monthlyUnpaidBalance + round(monthlyInterestRate * monthlyUnpaidBalance, 2), 2)
        amountPaid = round(amountPaid + minMonthlyPayment, 2)
        monthNum += 1
        return calcRemainingBalance(updatedBalance, annualInterestRate, monthlyPaymentRate, monthNum, amountPaid)

print('Remaining balance: {0}'.format(calcRemainingBalance(balance, annualInterestRate, monthlyPaymentRate, monthNum, amountPaid)))
