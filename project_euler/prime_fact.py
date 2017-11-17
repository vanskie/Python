import math

factors = []
primes = []
a = math.sqrt(600851475143)
a = math.ceil(a)
b = 600851475143

#making the factors list
for number in range(2,a):
	if b % number == 0:
		factors.append(number)

print(factors)

#Checking which of the factors are primes, and storing them in the list
#of factors
#But for our huge number 600851475143 this program will not work as it
#takes too long
#But we can use the square root of the number as there cannot
#be any more factors after the square root of the number

for number in factors:
	for i in range(2,number+2):
		if i != number and number % i == 0:
			break
		elif number == i:
			primes.append(number)
			break

		
		
print(max(primes))