#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
	last_digit = number % -10
	sign = -1
else:
	last_digit = number % 10
	print(f"Last digit of {number} is {last_digit}", end="")
last_digit = sign * number
if last_digit > 5:
	print(" and is greater than 5", end="")
elif last_digit == 0:
	print(" and is 0", end="")
elif last_digit < 6:
	print(" and is less than 6", end="")
	if last_digit != 0:
		print(" and not 0", end="")
print()
