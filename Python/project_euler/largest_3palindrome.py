def reverse(n):
	snumb = str(n)
	length = len(str(n))
	result = ''
	
	while length > 0:
		result += snumb[length-1]
		length -= 1

	result = int(result)
	return result
		
pali = []

for number1 in range(1000, 900, -1):
	for number2 in range(1000, 900, -1):
		a = number1 * number2
		b = reverse(a)
		if a == b:
			pali.append(a)
			break
		else:
			continue

print(pali)
print(max(pali))