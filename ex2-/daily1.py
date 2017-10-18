x = raw_input("Enter expression: ") # 4(x-y)-y^2-x^2+10
numbers = []
symNums = [] #list of all symbolic ints from 0 to 9 currently empty see line 6 fagit stuoid fagit
convert = 0
stringConvert = ""
print x # print ... tapak

for symb in range(0,10): #line 3 fagit
    symNums.append(str(symb))

for i in range(0,len(x)): # Checks if symbolic x[i] is in symNums if so it turns it into an int adn appends it to numbers but not any 2digit numbers go figure
    if x[i] in symNums:
        if type(int(x[i])) == type(int(x[i+1])):
            stringConvert = x[i] + x[i+1]
            convert = int(stringConvert)
            numbers.append(convert)
        numbers.append(int(x[i]))

print numbers
print symNums
