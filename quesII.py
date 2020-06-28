# Ques11

def count(s):
    d = dict()
    print(d)
    words = s.split()
    print(words)
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

test_string11 = input("enter sentence\t")
print(count(test_string11))


# Ques12

def cases(s):
    return s.upper(), s.lower()


test_string12 = input('enter string\t')
print(cases(test_string12))


# Ques 13

def comma(s):
    words13 = s.split(",")
    print(type(words13))
    words13.sort()
    return words13


test_string13 = input('enter comma separated words\t')
print(comma(test_string13))


# Ques 14


def htmlfxn(element, data):
    return '<{e}> {d} <{e}>'.format(e=element, d=data)


ele = input('enter element\t')
dt = input('enter data\t')
print(htmlfxn(ele, dt))


# Ques15

def insertString(element, string):
    return element[:2] + string + element[2:]


ele = input('enter element\t')
st = input('enter string\t')
print(insertString(ele, st))


# Ques 16

def summ(l):
    sum = 0
    for i in l:
        sum += i
    return sum


list16 = [1, 2, 3]
print(summ(list16))


# Ques17

def mul(l):
    mul = 1
    for i in l:
        mul *= i
    return mul


list16 = [1, 2, 3,4]
print(mul(list16))


# Ques18

def large(l):
    l.sort(reverse=True)
    return l[0]


list18 = [1,2,3,4,5,78,99]
print(large(list18))


# Ques19

def small(l):
    l.sort(reverse=False)
    return l[0]


list19 = [2,3,4,5,78,99]
print(small(list19))

# Ques20

def countstr(l):
    count = 0
    for i in range(len(l)):
        if l[i][0] == l[i][-1]:
            count += 1
    return count


test_list20 = ['abc', 'aba', 'xyz', '1221', 'abbba']
print(countstr(test_list20))
