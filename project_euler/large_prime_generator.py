
x = int(input('Enter, until which number you want the primes sum: '))
_list1 = []
result = 0
position = -1

for seed in range(3,x,2):
    _list1.append([seed, True])

for number in _list1:
    position += 1
    if True in number:
        for check in range(number[0] + position, len(_list1), number[0]):
           _list1[check] = [check, False]

for plus in _list1:
    if True in plus:
        result += plus[0]

print(result+2)


