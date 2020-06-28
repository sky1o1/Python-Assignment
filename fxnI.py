# FUNCTION

# Ques1 Write a Python function to find the Max of three numbers.

def max3(a, b, c):
    if a > b and a > c:
        return '{} is great'.format(a)
    elif b > a and b > c:
        return '{} is great'.format(b)
    else:
        return '{} is great'.format(c)


num1 = int(input("enter first num\t"))
num2 = int(input("enter second num\t"))
num3 = int(input("enter third num\t"))
print(max3(num1, num2, num3))


# Ques2 Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)

def sum2(l):
    return sum(l)


list2 = [8, 2, 3, 0, 7]
print(sum2(list2))

# Ques3 Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)

def mul3(l):
    mul_result = 1
    for i in l:
        mul_result *= i
    return mul_result


list3 = [8, 2, 3, -1, 7]
print(mul3(list3))


# Ques4 Write a Python program to reverse a string.
# Sample String : "1234abcd"

def revstr(s):
    print(s)
    list4 = list(s)
    list4.sort(reverse=True)
    new_str4 = "".join(list4)
    return new_str4


str4 = "1234abcd"
print(revstr(str4))


# Ques5 Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def fac(n):
    sample_num5 = 1
    if n == 0:
        return '1'
    else:
        for i in range(1, n+1):
            sample_num5 *= i
    return sample_num5


num5 = int(input("enter a num\t"))
print(fac(num5))


# Ques6 Write a Python function to check whether a number is in a given range.

def ran(n):
        if n in range(1, 10):
            return 'present'
        else:
            return 'not present'


num6 = int(input("enter a num to check\t"))
print(ran(num6))


# Ques7 Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'

def cases(s):
    countUpper = 0
    countLower = 0
    new_list7 = list(s)
    length7 = len(new_list7)
    for i in range(length7):
        if new_list7[i].isupper():
            countUpper += 1
        elif new_list7[i].islower():
            countLower += 1
        else:
            continue
    return countUpper, countLower


str7 = 'The quick Brow Fox'
print(cases(str7))

# Ques8 Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unq(l):
    length8 = len(l)
    new_list8 = []
    for i in range(length8):
        if l[i] not in new_list8:
            new_list8.append(l[i])
        else:
            continue
    return new_list8


list_8 = [1,2,3,3,3,3,4,5]
print(unq(list_8))

# Ques9 Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return 'not prime'
                break
            else:
                return 'prime'
                break
    else:
        return "not prime"


num9 = int(input("enter a num\t"))
print(prime(num9))


# Ques10 Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printeven(n):
    length_list10 = len(n)
    for i in range(1, length_list10):
        if i % 2 == 0:
            print(i)
        else:
            continue
    return 'even'


list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(printeven(list10))