#!/usr/bin/env python3

balance, annualInterestRate = 3926, 0.2

def payOffDebt(balance, annualInterestRate, remainingMonths, fixedMonthlyPayment):
    if remainingMonths == 0:
        if balance <= 0:
            return False
        else:
            return True
    else:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        remainingMonths -= 1
        return payOffDebt(updatedBalance, annualInterestRate, remainingMonths, fixedMonthlyPayment)

fixedMonthlyPayment = round(balance / 12, -1)
while payOffDebt(balance, annualInterestRate, 12, fixedMonthlyPayment):
    fixedMonthlyPayment += 10

print('Lowest Payment:', int(fixedMonthlyPayment))
