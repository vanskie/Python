import math

x = int(input('Enter number: '))
factors = []

if x > 100:
	for i in range(1, int(math.sqrt(x))):
	    if x%i == 0:
	        factors.append([i, int(x/i)])
else:
	for i in range(1, x):
		if x%i == 0:
			factors.append([i, int(x/i)])

print(sum(factors[-1]))
print(factors)
