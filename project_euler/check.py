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

'''

'''check = 0
a = True

while a:
    for i in range(100, 10000):
        for a in range(1,11):
            if i % a == 0:
                check += 1
                if check == 10:
                    print(i)
                    a = False
                    break
            else:
                print(i, 'check is ', check)
                check = 0
                continue

'''

'''string_set = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

set_list = []
result = 1
small_step = 0
big_step = 13
set_product = []
biggest_product = 0
char_holder = 0

for i in range(0,1000):
    b = []

    for y in range(small_step, big_step):

        if y >= len(string_set):
            break

        b.append(int(string_set[y]))

        if y == big_step - 1:
            small_step += 1
            big_step += 1

    set_list.append(b)

result = sum(set_list[0])

for x in set_list:
    for i in range(0,len(x)):
        result *= x[i]
    set_product.append(result)
    result = 1

biggest_product = set_product[0]



for u in range(0, len(set_product)-1):
    if set_product[u] > biggest_product:
        biggest_product = set_product[u]
        char_holder = u

print(biggest_product)
print(set_list[char_holder])
print(char_holder, '\n')
print(set_product)
'''
import math

a1 = 1
b1 = 0
c1 = 1

a2 = 2
b2 = 0
c2 = 2
b22 = 3
c22 = 3
result = 0
result1 = 0

for i in range(1,1000):
    a1 += 2
    b1 += 1
    c1 += 1
    if math.sqrt(a1) % 1 == 0:
        print('\t',int(math.sqrt(a1)), b1, c1,'\n')
    if a1+b1+c1 == 1000:
        result = a1 * b1 * c1
        break

for y in range(1,100):
    a2 += 2
    b2 += b22
    c2 += c22
    print('\t',a2, b2, c2, '\n')
    b22 += 2
    c22 += 2
    if a2+b2+c2 == 1000:
        result1 = a2 * b2 * c2
        break
'''
'''
'''


_list1 = list(range(2,100))
_list2 = []
count = -1

for number in _list1:
    if number == 13:
        break
    count += 1
    if number in _list2:
        continue
    else:
        for check in range(count + number, len(_list1), number):
            _list2.append(_list1[check])

_list2.sort()

for delete in _list1:
    if delete in _list2:
        _list1.remove(delete)


print(_list1)
print('\n', _list2)


