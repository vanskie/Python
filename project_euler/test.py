'''import time

start_time = time.time()
x = int(input('Enter \'till which number you want primes'))
_list1 = list(range(3,x,2))
_list2 = []
count = -1

for number in _list1:
    count += 1
    if number * number <= _list1[-1]:
        for check in range(count + number, len(_list1), number):
            if _list1[check] not in _list2:
                _list2.append(_list1[check])
                print('\n Adding to list 2 (crossed list)', _list1[check], end = ' ')

    else:
        continue
            
_list2.sort()

for delete in _list2:
    if delete in _list1:
        _list1.remove(delete)
        #print('\ndeleting', _list1[delete])
    print('delete = ', delete, '\nThe len of _list1 = ', len(_list1), '\nThe len of _list2 = ', len(_list2))

print('\n',sum(_list1) + 2)
print(time.time())
'''

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



