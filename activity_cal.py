# CS362_Winter21
# Class Activity
# Program: activity_cal.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that implements a calculator.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 activity_cal.py
###########################################################################

def cal_add(a, b):
    return a + b

def cal_sub(a, b):
    return a - b

def cal_mul(a, b):
    return a * b

def cal_div(a, b):
    return a / b
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("add: ", cal_add(num1, num2))
print("sub: ", cal_sub(num1, num2))
print("mul: ", cal_mul(num1, num2))
print("div: ", cal_div(num1, num2))
