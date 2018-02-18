import time

t0 = time.time()
primes = [2,]
place = 10001
max = 10
min = 1
check = 1

while len(primes) <= place:
	for i in range(min,max):
		for y in range(1,i):
			if i % y != 0:
				check += 1
				if check == i-1 and len(primes) != place:
					primes.append(i)
					print('number = ', i, 'check =', check, 'current list length', len(primes))
				elif len(primes) == place:
					break
			else:
				check = 1

	if len(primes) != place:
		min = max
		max *= 10
	else:
		print(primes)
		print('Length of primes list is ', len(primes))
		print(primes[-1])
		break
t1 = time.time()

print(t1 - t0)
print((t1 - t0) / 60)

'''Length of primes list is  10000
104729
2353.1099865436554
39.21849977572759
 
for place 10000 you idiot
'''