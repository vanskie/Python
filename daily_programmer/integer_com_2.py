def factor(number):
	factors = []
	if number < 1000:
		for i in range(1, number):
			if number%i == 0:
				factors.append([i, int(number/i)])
	else:
		for i in range(1, int(number**0.5)):
			if number%i == 0:
				factors.append([i, int(number/i)])
	return factors

def smallestComp(number):
	factors = factor(number)
	if len(factors) == 1 and factors[0][1] >= 4:
		return smallestComp(number-1) + 1
		#if smallestComp(number-1) + 1 < smallestComp(number+1):
			#return smallestComp(number-1)
		#else:
			#return smallestComp(number+1) 
	if factors == 1:
		smallSum = 1
		smallPro = 1
	else:
		#TODO: Make this work for 1 as well
		smallSum = factors[0][1]
		smallPro = factors[0][1]
	
	for element in factors:
		if sum(element) < smallSum:
			smallSum = sum(element)
		if element[0] * element[1] < smallPro:
			smallPro = element[0] * element[1]

	if smallSum < smallPro:
		return smallSum
	else:
		return smallPro

for i in range(2, 21):
	print(i, smallestComp(i))



