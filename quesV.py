# Ques40

def tupadd(t, val):
    list40 = list(t)
    list40.append(val40)
    tup40 = tuple(list40)
    return tup40



tup40 = (1, 3, 5, 7, 9, 2, 4, 6, 8)
val40 = int(input("enter value to be added\t"))
print(tupadd(tup40, val40))


# Ques41

def tupstr(t):
    print(t)
    str41 = " ".join(t)
    return str41


tup42 = ('a', 'b', 'c', 'd', 'e')
print(tupstr(tup42))


# Ques42

def tuplist(l):
    print(l)
    tup42 = tuple(l)
    return tup42


list42 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(tuplist(list42))


# Ques43

def tuprmv(t, val):
    list43 = list(t)
    list43.remove(val)
    tup43 = tuple(list43)
    return tup43


tuple43 = (1, 3, 5, 7, 9, 2, 4, 6, 8)
print(tuple43)
val43 = int(input("enter a value to be removed\t"))
print(tuprmv(tuple43, val43))


# Ques44

def tupslice(t):
    return t[0:5], t[5:]

tuple44 = (1, 3, 5, 7, 9, 2, 4, 6, 8)
print(tupslice(tuple44))


# Ques45

def tupind(t, v):
    if v in t:
        return "index is:", t.index(v)
    else:
        raise IndexError


tuple45 = (1, 3, 5, 7, 9, 2, 4, 6, 8)
print(tuple45)
val45 = int(input("enter a value\t"))
print(tupind(tuple45, val45))

# Ques46

def tuplen(t):
    len46 = len(t)
    return "length is:", len46


tuple46 = (1, 3, 5, 7, 9, 2, 4, 6, 8, 10)
print(tuplen(tuple46))