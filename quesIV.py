# Ques31

def iterate(d):
    print(d.keys())
    print(d.values())
    for x, y in zip(d.keys(), d.values()):  #in d.items
        print(x, y)
    return


d31 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(iterate(d31))


# Ques32

def dictcons(n):
    new_dict = dict()
    for i in range(1, n+1):
        new_dict[i] = i*i
    return new_dict


test_dict32 = int(input("enter sample number\t"))
print(dictcons(test_dict32))


# Ques33

def dictcons(n):
    new_dict = dict()
    for i in range(1, n+1):
        new_dict[i] = i*i
    return new_dict


test_dict32 = 15
print(dictcons(test_dict32))


# Ques34

def mergedict(d1, d2):
    d1.update(d2)
    return d1


diction1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
diction2 = {7: 1, 8: 9, 10: 9}
print(mergedict(diction1, diction2))


# Ques35

def dictiter(n):
    length_dict35 = len(n)
    for i, j in n.items():
        result = '{x} : {y}'.format(x=i, y=j)
    return result

test_dict35 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,
13: 169, 14: 196, 15: 225}
print(dictiter(test_dict35))


# Ques36

def dictsum(d):
    sum_key = sum(d.keys())
    sum_val = sum(d.values())
    sum_items = sum_key + sum_val
    return sum_items


test_dict36 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dictsum(test_dict36))


# Ques37

def dictmul(d):
    mul_data1 = 1
    mul_data2 = 1
    for i, j in d.items():
        mul_data1 *= i
        mul_data2 *= j
    return mul_data1, mul_data2


test_dict37 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dictmul(test_dict37))


# Ques38

def dict_pop(d, k):
    d.pop(k)
    return d


test_dict38 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(test_dict38)
test_key38 = int(input("enter a key to delete\t"))
print(dict_pop(test_dict38, test_key38))


# Ques39

def unpack(t):
    a, b, c = t
    print(a)
    print(b)
    print(c)
    return 'result'

tup39 = (1, 2, 3)
print(unpack(tup39))