#Now we use list comprehension to print out the first 10 cubes.
cubes = [cube**3 for cube in range(1,11)]
print(cubes)
#This is now example4-10:

print('\nThe first three items in the list are: ', cubes[0:3])
print('\nThree items from the middle of the list are: ', cubes[3:6])
print('\nThe last three items in the list are: ', cubes[-3:])