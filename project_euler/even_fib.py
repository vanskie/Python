'''fib = [1, 2]

for step in range(0,4000000):
	if step < 1:
		pass
	if step >= 1:
		fib.append(fib[step] + fib[step-1])

print(sum(fib))

This gives me a memory error:

$ python3 even_fib.py
Traceback (most recent call last):
  File "even_fib.py", line 7, in <module>
    fib.append(fib[step] + fib[step-1])
MemoryError
'''

'''a = 1
b = 2
c = 0
i = 0
result = 0

while i < 8:
	c = b + a
	a = b
	b = c
	print(c)
	if c % 2 == 0:
		result += c

	i += 1

print(result)
'''

fib = [1,2]
step = 1

while True:
	fib.append(fib[step] + fib[step-1])
	if fib[step-1] % 2 == 0:
		step += 1
	else:
		del fib[step-1]
	if sum(fib) > 4000000:
		break

print(sum(fib))