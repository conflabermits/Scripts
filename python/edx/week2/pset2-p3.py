#!/usr/bin/env python3

balance = 320000
annualInterestRate = 0.2

epsilon = 0.0101
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

def getMiddle(lower, upper):
    return round(lower + (upper - lower) / 2, 2)

def payOffDebt(balance, annualInterestRate, remainingMonths, fixedMonthlyPayment):
    if remainingMonths == 0:
        return balance
    else:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        remainingMonths -= 1
        return payOffDebt(updatedBalance, annualInterestRate, remainingMonths, fixedMonthlyPayment)

fixedMonthlyPayment = getMiddle(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

while True:
    endBalance = payOffDebt(balance, annualInterestRate, 12, fixedMonthlyPayment)
    if abs(endBalance) <= epsilon:
        break
    elif abs(monthlyPaymentUpperBound - monthlyPaymentLowerBound) <= epsilon:
        if abs(payOffDebt(balance, annualInterestRate, 12, monthlyPaymentLowerBound)) < abs(payOffDebt(balance, annualInterestRate, 12, monthlyPaymentUpperBound)):
            fixedMonthlyPayment = monthlyPaymentLowerBound
        else:
            fixedMonthlyPayment = monthlyPaymentUpperBound
        break
    else:
        if endBalance > epsilon:
            monthlyPaymentLowerBound = fixedMonthlyPayment
            fixedMonthlyPayment = getMiddle(monthlyPaymentLowerBound, monthlyPaymentUpperBound)
        else:
            monthlyPaymentUpperBound = fixedMonthlyPayment
            fixedMonthlyPayment = getMiddle(monthlyPaymentLowerBound, monthlyPaymentUpperBound)

print('Lowest Payment:', fixedMonthlyPayment)
