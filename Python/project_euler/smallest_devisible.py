'''
We can start by checking each number if its devisible by 1, 5 - many will fall,
but if it is devisible by 1,5 then we check from 5, to 10 and then from 
10 to 20
'''

min = 99999999
max = 1000000000
check = 0

while True:
	for number in range(min,max):
		for mod in range(1,21):
			if number % mod == 0:
				check += 1
				print(number, mod)
				if check == 20:
					print('\n\t\t\t\t', number)
					break
			else:
				check = 0
				continue
			
		
	break