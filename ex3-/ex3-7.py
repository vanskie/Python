invites = ['Tesla', 'Einstein', 'A translator for Einstein(probably my wife :))']
invite_message = "God bless, you are invited for dinner "
#Making a list with names
print(invite_message, invites[0] + '.')
print(invite_message, invites[1] + '.')
print(invite_message, invites[-1] + '.')
print(invites[0] + " and " + invites[1] + " cannot attend the dinner due to death.")

invites[0] = "Lalo"
invites[1] = "Mam"
invites[2] = "Zori"
#Changing the values of the list

print(invite_message, invites[0] + '.')
print(invite_message, invites[1] + '.')
print(invite_message, invites[2] + '.')
print("\n\n\n\t\t\t\tBUT WAIT I FOUND A BIGGER TABLE, NOW EVERYBODY CAN COME!!!")

invites.insert(0, 'Roska')
invites.insert(2, 'Gicho')
#Inserting new items in the list in specific indeces.
invites.append('Jij')
invites.append('Eka')
#Appending two new items in the end of the list.

print(invite_message, invites[0])
print(invite_message, invites[1])
print(invite_message, invites[2])
print(invite_message, invites[3])
print(invite_message, invites[4])
print(invite_message, invites[5])
print(invite_message, invites[6])

print("\n\n\n\t\t\t\t\n\n\nOH SHNITZEL THE TABLE WONT ARRIVE ON TIME, I HAVE ROOM FOR ONLY TWO PEOPLE.")

uninvited_message = "Im so sorry to uninvite you "
uninvited_person1 = invites.pop(0)
#Storing an item from the list that we are removing with the pop methon, in a variable
print(uninvited_message, uninvited_person1)
#The list now is shorter by one so, when we want to remove the second person from the list also
#We will once again pop(0) as before because now the list is shorter.

uninvited_person2 = invites.pop(0)
print(uninvited_message, uninvited_person2)

uninvited_person3 = invites.pop(0)
print(uninvited_message, uninvited_person3)

uninvited_person4 = invites.pop(2)
print(uninvited_message, uninvited_person4)

uninvited_person5 = invites.pop(2)
print(uninvited_message, uninvited_person5)

print(invites[0] +', ' + invites[1] + " I'm happy to say you're still invited :).")

del invites[0]
del invites[0]
#Now we delete the last two items in the list to check if we used everything in the list.

print(invites)
