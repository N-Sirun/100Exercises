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

 #Ex25