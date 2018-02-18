nato_alphabet = ['Delta', 'Alpha', 'Charlie', 'Bravo']

print(nato_alphabet)
print(sorted(nato_alphabet))
print('To show that the list is still in its original order we simply print it:\n', nato_alphabet)
print('Printing the list in reverse alphabetial order with the sorted function:\n', sorted(nato_alphabet, reverse = True))
print('To show that the list is still in its original order after the sorted function:\n', nato_alphabet)
nato_alphabet.reverse()
print('Using the reverse method we permanently change the list order to reverse(meaning that we reverse the order of how the items were introduced):\n',
	nato_alphabet, '\n The list was reversed earlier, not when we printed it')
nato_alphabet.reverse()
print('\n We reverse the order of the list again to revert to the original order:\n', nato_alphabet)
nato_alphabet.sort()
print('\n We now use the sort method to permanently change to alphabetical order:\n', nato_alphabet)
nato_alphabet.sort(reverse = True)
print('\n We now use sort again but to permanently change the list to reverse alphabetical order:\n', nato_alphabet)
