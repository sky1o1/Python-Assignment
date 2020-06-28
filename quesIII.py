# Ques21


def tup(l):
    return sorted(l, key=lambda x: x[-1], reverse=False)


test_tup21 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(tup(test_tup21))

# Ques22


def remove(dup):
    new_list = []
    for i in dup:
        if i not in new_list:
            new_list.append(i)
    return new_list


test_list22 = ['1', '1', '2', '3', '4', '4']
print(remove(test_list22))


# Ques23

def check(l):
    if not l:
        return 'empty'
    else:
        return 'not empty'

test_list23 = []
print(check(test_list23))

# Ques24

def clone(lis):
    clone_list = list(lis)
    return lis, clone_list


test_list24 = [1, 2, 3, 4, 5]
print(clone(test_list24))


# Ques25

def dict(d):
    for i in d:
        if not i:
            return 'True'
        else:
            return 'False'


test_list25 = [{},{},{}]
print(dict(test_list25))

# Ques26

def insert(l, string1):
    new_list = []
    for i in l:
        list1 = i
        new_list.append('{s}{li}'.format(s=string1, li=list1))
    return new_list


test_list26 = [1, 2, 3, 4]
test_string26 = 'emp'
print(insert(test_list26, test_string26))


# Ques27

def replace(l1, l2):
    l1.pop()
    l3 = l1 + l2
    return l3


list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
print(replace(list1, list2))


# Ques28

def diction(d1, k1, v1):
    d1.update({k1:v1})
    return d1


dict1 = {0: 10, 1: 20}
key1 = input("enter key\t")
val1 = input("enter value\t")
print(diction(dict1, key1, val1))


# Ques29

def add_dict(d1, d2, d3):
    d1.update(d2)
    d1.update(d3)
    return d1


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(add_dict(dic1, dic2, dic3))


# Ques30

def checkdict(k, d):
    print(d.keys())
    print(type(d.keys()))
    if k in d:
        return 'present'
    else:
        return 'not present'


d30 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key30 = int(input("enter key\t"))
print(checkdict(key30, d30))