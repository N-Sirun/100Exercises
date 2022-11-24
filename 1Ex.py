 #Ex 2
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
#
# print("Addition: ",(num1+num2))
# print("Subtraction: ",(num1-num2))
# print("Multiplication: ",(num1*num2))
# print("Division: ",(num1/num2))

 #Ex 3
# import math
# number = int(input("Enter any number : "))
# print("Square root of ", number, " is ", math.sqrt(number))

 # Ex 4
# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))
# temp = x
# x = y
# y = temp
# print("The value of x after swapping is {}".format(x))
# print("The value of y after swapping is {}".format(y))
# x, y = y, x
# print("The value of x after swapping is ", x)
# print("The value of y after swapping is ", y)

 #Ex 5
# for n in range(7):
#      print("Hello")
#print("Hello\n" * 7)


 #Ex 6
# import random
# print(random.randint(1, 100))

 #Ex 7
# num = int(input("Enter any number to test whether it is odd or even: " ))
# if (num % 2) == 0:
#     print(num, " is even")
# else:
#     print(num, " is odd")

 #Ex 8
# my_list = [2, 5, 6, 84, 240, 25, 152, 421, 325]
# print(max(my_list))

 #Ex 9
# num = int(input("Enter any number to check its' prime or not: "))
# counter = 0
#
# for x in range(2, num):
#     if (num % x == 0):
#         counter = counter + 1
#
# if (counter==0):
#     print("It's prime number")
# else:
#     print("It's not prime number")


 #Ex 10
# import math
# number = 7
# print(math.factorial(number))

# Solution 2
# number = int(input("Enter any number: "))
# fact = 1

# for x in range(1, number+1):
#     fact = fact * x
# print("Factorial of ", number, " is:", fact)

 #Ex 11
# letter = input("Enter a character: ")
# print("ASCII value of ", letter, " is:", ord(letter))

 #Ex12
# import datetime
# today = datetime.date.today()
# print("Today's date is: ", today)

 # Ex13
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
#
# for i in range(len(X)):
#
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)

 #Ex15
# list = ["g","d","r","j","a","e"]
# sorted = list.sort()
# print(list)

 #Ex16
# from statistics import mode
# list1 = [2,5,4,7,8,1,8,1,9,8,9,8,3,8,]
# frequent_num = mode(list1)
# print("Most frequent number is: ", frequent_num)

 #Ex17

# a = 14
# b = 8
# c = 10
# s = (a + b + c) / 2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print("Area of triangle is: ", area)

 #Ex18

# name = "James"
# last = "Bond"
# print(f'Hi, I am {last}, {name} {last}... Nice to meet you! ')
#
# kilometres = 6.7
# conversion = 0.621371
# miles = kilometres * conversion
# print(miles)

 #Ex19

# import calendar
# yy = 1986
# mm = 12
# print(calendar.month(yy, mm))

 #Ex20

# year = int(input("Enter the year: "))
#
# if (year % 400) == 0 and (year % 100) == 0:
#     print(f'{year} Year is leap year')
# elif (year % 4) == 0 and (year % 100) != 0:
#     print(f'{year} Year is leap year')
# else:
#     print(f'{year} is not leap year')

 #Ex21

# n = int(input("Enter positive number: "))
# n = int(n * (n + 1) / 2)
# print(f'Sum of natural number is: {n}')

 #Ex22

# def find_lcm(x, y):
#     if x > y:
#         greater = x
#     else: greater = y
#
#     while (True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#         greater += 1
#     return lcm
# num1 = 2
# num2 = 3
# print("The LCM of number is:", find_lcm(num1, num2))

 #Ex24

# my_str = "Hello, I am super programmer of python language."
# words = [word.upper() for word in my_str.split()]
# words.sort()
# print("The sorted words are: ")
# for word in words:
#     print(word)

 #Ex25 Ex26

# list1 = ['f', 'g', 'i', 'o', 'a', 'e', 'f', 'x', 'd']
# sorted_list = sorted(list1)
# desc_order = sorted(list1, reverse=True)
# print("The sorted letters are: ", sorted_list)
# print("The sorted letters in descending order are: ", desc_order)


 #Ex27 Ex28

# for i in range(2, 20, 2):
#
#     print(i)
# for num in range(1, 20, 2):
#     print(num)

 #Ex28

# lower = 1
# upper = 30
# print(f'All prime numbers between {lower} and {upper} are:')
# for num in range(lower, upper + 1 ):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

 #Ex31

# string_my = "Hello, I am the greatest, super programmer!"
# print(string_my.replace(",", ""))

 #Ex32

# list1 = ['f','g', 'g', 'y', 'o', 'y', 'o', 'a']
# print(list1)
# print(list(dict.fromkeys(list1)))
# print(list(set(list1)))

 #Ex33 Ex34

# list1 = [200,38,4,7,4,5,66,4,88,13,22,55,70,5]
# print("The smallest number is: ", min(list1))
# print("The largest number is: ", max(list1))

 #Ex35
# ch = str(input("Enter any single letter: "))
# if (ch =='a' or ch== 'e' or ch== 'i' or ch =='o' or ch== 'u'
# or ch =='A' or ch== 'E' or ch== 'I' or ch=='O' or ch== 'U' ):
#     print(f"Character {ch} is vowel")
# else:
#     print(f"Character {ch} is consonant")

 #Ex36
# list1 = [1,2,7,3,4,8,9]
# print(sum(list1))

 #Ex37
# num = int(input("Enter number: "))
# print(len(str(num)))

 #Ex38

# list1 = [2,8,3,4,2,8,3,8,7,9,2,3,5,11,92,73]
# unique_list1 = list(set(list1))
# print(unique_list1)

 #Ex39 Ex40
# string1 = "I am python auto engineer"
# count_words = len(string1.split())
# print(count_words) #counting words in string
# print(string1.count("o")) #counting specific letters in string

 #Ex41

# str1 = "I want to become python test automation engineer"
# str2 = len(str1.split())
# if len(str1) == 0:
#     print("The string is empty")
# else:
#     print(f"The string contains {str2} words")

 #Ex42

# str1 = "222310"
# print(int(str1))

 #Ex43
# str1 = "HelloPretty"
# print(str1[::-1])

 #Ex44

# str1 = ["I", "want", "to", "become", "an", "engineer"]
# print(" ".join(str1))

 #Ex45 Ex46
# str1 = "hello i am very nice person"
# print(str1.upper())
# str2 = "HERE ARE MY STRINGS"
# print(str2.lower())

 #Ex47 Ex48

# print("\t * \n\t* *\n   * * *\n  * * * *\n * * * * *")
# print("")
# print(" * * * * * *\n  * * * * *\n   * * * *\n\t* * *\n\t * *\n\t  * ")
#print("*****\n*****")

 #Ex54

# ascii_num = 65
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i * 1):
#         character = chr(ascii_num)
#         print(character, end=' ')
#         ascii_num += 1
#     print("")

 #Ex55
# list1 = ["d", "r", "y", "a", "w"]
# list1.pop(1)
# print(list1)

 #Ex56

# minutes = int(input("Enter minutes to convert into seconds: "))
# conversion_rate = 60
# seconds = conversion_rate * minutes
# print(f"{minutes} minutes are {seconds} seconds")

 #Ex57

# hours = int(input("Enter hours to convert into seconds: "))
# conversion_rate = 3600
# seconds = conversion_rate * hours
# print(f"{hours} minutes are {seconds} seconds")

 #Ex58

# from datetime import datetime
#
# str_d1 = '2013/01/02'
# str_d2 = '2022/11/23'
#
# d1 = datetime.strptime(str_d1, "%Y/%m/%d")
# d2 = datetime.strptime(str_d2, "%Y/%m/%d")
# delta = d2 - d1
# print(f'Difference between dates are: {delta.days} days')

 #Ex59

# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,10]
# new_list = list1 + list2
# print(new_list)
#
# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,10]
# list1.extend(list2)
# print(list1)

 #Ex60 Ex61

# decimal = 78
# new_bin = bin(decimal).replace('0b', '')
# print(int(new_bin))
# n = "1101001"
# decimal_number = int(n, 2)
# print(decimal_number)


