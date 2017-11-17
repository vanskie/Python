'''pali = []
multiples = list(range(100, 1000))
result = []

for number in range(10000,1000001):
	snumb = str(number)
	for i in range(0,len(snumb)):
		if snumb[-1] == snumb[0] and snumb[-2] == snumb[1] and snumb[-3] == snumb[2]:
			pali.append(number)
			break
		else:
			pass

print(pali)
print(len(pali))

for i in range(1000, 900, -1):
	for y in multiples:
		if i * y in pali:
			print('\n', i, y, '=', i*y, '\n\n')
			result.append(i*y)

print('\n\n\n\t', max(result))
'''

import time
start_time = time.time()
def find_reverse(n):
    ori = int(n)
    length = len(str(n))
    reverse = 0
    while length > 0:
        reverse += (ori % 10) * (10 ** (length - 1))
        ori = int(ori / 10)
        length -= 1
    return(reverse)
max = 999
min = 900
num = 0
while min >= 100:
    for n in range(max, min, -1):
        for x in range(max, min, -1):
            num = n * x
            if num == find_reverse(num):
                break
        else:
            continue
        break
    else:
        max = max - 100
        min = min - 100
        continue
    break
print(num)
print("This took", time.time() - start_time, "seconds to run.")