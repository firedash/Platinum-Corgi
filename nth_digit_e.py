#Calculating Euler's number to n digits using Newton's series expansion 

import math 

i=1 #iterator, used to check when we reach desired precision 
e_val = 1 
e_digits = int(input('Number of digits to generate: '))
while True:
	if 1/math.factorial(i) < 10**(-e_digits):
		break
	e_val += 1/math.factorial(i)
	i += 1

print(str(round(e_val,e_digits+1))[:-1]) #Round by itself didn't work, rounding to an extra digit and truncating it later