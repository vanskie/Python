'''numbers = list(range(1,1000))
result = 0
for number in numbers:
	if number %3 == 0 or number %5 == 0:
		#print(number)
		result += number
		
#print(numbers)
print(result)
'''

result = 0
for number in range(1,1000):
	if number %3 == 0 or number %5 == 0:
		result += number

print(result)
