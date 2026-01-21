#!/usr/bin/python3
import sys
"""
Calculate the factorial of a given non-negative number recursively

args:
	n (int): The non-negative integer to calculate the factorial of

Returns:
int: The factorial of the input
	Returns 1 if n is 0
"""
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
