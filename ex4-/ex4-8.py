#The cubes of the numbers from 1 through 10.
cubes = []
for number in range(1,11):
	cubes.append(number**3)
	print(cubes[number-1])