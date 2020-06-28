
# Ques11 Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

def lamb(x, y):
    a = lambda x: x + 15
    sum11 = a(x)
    b = lambda x, y: x * y
    mul11 = b(x, y)
    return sum11, mul11


print(lamb(2, 4))


# Ques12 Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def mulunknown(n, y):
    result12 = lambda x: x * n
    return result12(y)


num12 = int(input("enter a num\t"))
var12 = int(input("enter a variable\t"))
print(mulunknown(num12, var12))


# Ques13 Write a Python program to sort a list of tuples using Lambda.

def sortlambda(n):
    n.sort(key=lambda x: x[1])
    return n


tuple13 = [('ram', 95), ('shyam', 85), ('sita', 93), ('gita', 77)]
print(sortlambda(tuple13))


# Ques14 Write a Python program to sort a list of dictionaries using Lambda.

def sortdict(d):
    sort14 = sorted(d, key=lambda x: x[1])
    return sort14


dict14 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(sortdict(dict14))


# Ques15

def filt(l):
    result15 = list(filter(lambda x: x % 2 == 0, l))
    return result15


list15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filt(list15))


# Ques16 Write a Python program to square and cube every number in a given list of
# integers using Lambda.

def sq(n):
    length16 = len(n)
    for val in n:
        square16 = lambda x: x ** 2
        cube16 = lambda x: x ** 3
        print(square16(val), cube16(val))
    return 'result'


list16 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sq(list16))


# Ques17 Write a Python program to find if a given string starts with a given character
# using Lambda.

def startlambda(s, i):
    low = s.lower()
    print(low)
    str17 = lambda x: True if x.startswith(i) else False
    return str17(low)


test_str17 = 'Assignment'
inp_str = input("enter a string\t")
print(startlambda(test_str17, inp_str))


# Ques18 Write a Python program to check whether a given string is number or not
# using Lambda.

def num1(s):
    str18 = lambda x: 'Number' if x.isdigit() else 'String'
    return str18(s)


string18 = input("enter a string\t")
print(num1(string18))


# Ques19 Write a Python program to create Fibonacci series upto n using Lambda.

def fib():
    num1 = 1
    num2 = num1
    result = 0
    tool = lambda x, y: x + y
    return tool(num1, num2)


print(fib())


# Ques20 Write a Python program to find intersection of two given arrays using Lambda.

def inter(a1, a2):
    print(a1)
    print(a2)
    result = list(filter(lambda x: x in a1, a2))
    return "intersection is:", result


arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
arr2 = [2, 4, 6, 8, 10]
print(inter(arr1, arr2))

