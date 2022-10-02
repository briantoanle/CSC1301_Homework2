# Prolog
# Author: TOAN LE
# Email: tle153@student.gsu.edu
# Section: 036

# supply program prolog (3 P's)
# main function
# Display introductory message
# Your design here............

"""
    Purpose:
        Python program to check prime number
    Pre-conditions (input):
        any integer (integer) = number_to_check
    Post-conditions (output):
        If number_to_check is a prime number, display:
            'The integer ' + num_str + ' is prime.'
        If number_to_check is a negative number, display:

    Design:
        Import sympy per assignment requirement
        Define a function called findPrime that uses sympy's isPrime method to check for prime number
            function will return true or false

        Prompt user to enter an integer, store value as an integer in variable number_to_check
        Concatenate number_to_check to string and store it in variable num_str to use later when displaying output

        if statement, call function findPrime to check for prime number, if it returns true,
            then print integer num_str is prime
        else if statement, check to see if number is a negative number or not by comparing to 0.
            if it is less than 0, print integer num_str is negative
        else statement, print integer num_str is not prime if the other 2 if statements are not satisfied

"""
