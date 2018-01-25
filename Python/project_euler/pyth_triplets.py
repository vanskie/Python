storage = []
slip = []
product = 1

for p in range(2,100):
    for q in range(1,p):
        if p % 2 == 0 or q % 2 == 0 and len(slip) == 3:
            a = 2 * p * q
            b = pow(p,2) - pow(q,2)
            c = pow(p,2) + pow(q,2)
            slip.append(a)
            slip.append(b)
            slip.append(c)
            slip.sort()
            storage.append(slip)
            slip = []
            slip.append(a*2)
            slip.append(b*2)
            slip.append(c*2)
            slip.sort()
            storage.append(slip)
            slip = []
        else:
            a = p * q
            b = (pow(p,2) - pow(q,2)) / 2
            c = (pow(p,2) + pow(q,2)) / 2
            slip.append(a)
            slip.append(b)
            slip.append(c)
            slip.sort()
            storage.append(slip)
            slip = []
            slip.append(a*2)
            slip.append(b*2)
            slip.append(c*2)
            slip.sort()
            storage.append(slip)
            slip = []


for i in range(0,len(storage)):
    if sum(storage[i]) == 1000:
        print(storage[i])
        for k in storage[i]:
            product *= k
        break

print(product)
