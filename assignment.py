# Ques1 Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'

str1 = 'google.com'
freq = {}

for char in str1:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Char frequency in '{}' is :\n {}".format(str1, str(freq)))


# Ques2 Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'

def ques2(x):
    if len(x) < 2:
        return 'empty'
    else:
        return x[0:2] + x[-2:]


inp = input('enter a word \n')
print(ques2(inp))


#Ques3

def replace(x):
  char = x[0]
  x = x.replace(char, '$')
  x = char + x[1:]
  return x

str1 = input('enter a word \t')
print(replace(str1))


# Ques4 Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'

def swap(x, y):
    combined_str = x + ' ' + y
    x1 = y[0:2] + x[2:]
    y1 = x[0:2] + y[2:]
    swaped_str = x1 + ' ' + y1
    return combined_str, swaped_str


strin1 = input('enter first string \t')
strin2 = input('enter second string \t')
print(swap(strin1, strin2))


#Ques5

def ing(x):
    if len(x) < 3:
        return x
    elif len(x) >= 3:
        if x[-3:] == 'ing':
            return x + 'ly'
        else:
            return x + 'ing'


test_string5 = input('enter a word \t')
print(ing(test_string5))

# Ques6
def good(str6):
    string_not = str6.find('not')
    string_poor = str6.find('poor')

    if string_poor > string_not and string_not > 0 and string_poor > 0:
        str6 = str6.replace(str6[string_not:(string_poor + 4)], 'good')
        return str6
    else:
        return str6


print(good('The lyrics is not that poor!'))
print(good('The lyrics is poor!'))


# Ques7 workflow -> The function asks for the input until the user types /end.
# Then the function sorts the longest word in the list

list1 = []


def long_list():
    while True:
        test_string7 = input('enter words \t')
        if test_string7 != '/end':
            list1.append(test_string7)
        else:
            break
    print(type(list1))
    list1.sort(key=len, reverse=True)
    return list1[0]

print(long_list())


# Ques 8

def rmv(s, n):
    new_str8 = ""
    list8 = list(s)
    list8.remove(list8[n])
    return new_str8.join(list8)


str8 = input("enter a string\t")
print(str8)
rmv_ind = int(input("enter the index to remove\t"))
print(rmv(str8, rmv_ind))


# Ques9

def swaped(x):
    lists = list(x)
    print(type(lists))
    temp = lists[0]
    lists[0] = lists[-1]
    lists[-1] = temp
    j = "".join(lists)
    return j


test_string9 = input('enter a string\t')
print(swaped(test_string9))

# Ques 10

def odd(x):
    list_10 = list(x)
    new_list10 = []
    length_of_x = len(list_10)
    print(list_10)
    for i in range(length_of_x):
        if i % 2 != 0:
            new_list10.append(list_10[i])
            result10 = " ".join(new_list10)
        else:
            continue
    return result10


test_string10 = input("enter a string\t")
print(odd(test_string10))












