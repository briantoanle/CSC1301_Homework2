# Prolog
# Author: Toan Le
# Email: tle153@student.gsu.edu
# Section: 036
# CRN: 84165
# Assignment: CSC 1301 Homework 2 isPrime

# supply program prolog (3 P's)
"""
    Purpose:
        Python program to check prime number
    Pre-conditions (input):
        any integer (integer) = number_to_check
    Post-conditions (output):
        If number_to_check is a prime number, display:
            'The integer ' + num_str + ' is prime.'
        If number_to_check is a negative number, display:

"""
# import sympy
from sympy import *

# define function findPrime that takes an integer as input and returns a boolean value
def findPrime(num):

    # call sympy's function isPrime and pass in variable num
    return isprime(num)

#   main function
def main():

    # Display introductory message
    print("   ***   isPrime   ***")

    # Prompt user to enter an integer, store value as an integer in variable number_to_check
    number_to_check = int(input("Please provide an integer: "))

    # Concatenate number_to_check to string and store it in variable num_str to use later when displaying output
    num_str = str(number_to_check)

    # call function findPrime to check for prime number, if it returns true, then print integer num_str is prime
    if findPrime(number_to_check):
        print('The integer ' + num_str + ' is prime.')

    # if findPrime returns false, check to see if number is a negative number or not by comparing to 0.
    #   if it is less than 0, print integer num_str is negative
    elif number_to_check < 0:
        print('The integer ' + num_str + ' is negative.')

    # if both conditions above returns false, print integer num_str is not prime
    else:
        print('The integer ' + num_str + ' is not prime.')



main()