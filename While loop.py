# for name in 'string':
#     if name == 'g':
#         break
#     print(name)
#
# age = 1
#
# while age < 18:
#     print(age, "You are still a minor")
#     age += 1
#     if age == 18:
#         print(age, "You are now a major")
#
# value = 'hollywood'
# if value == 'w'':
#     print('detected w')

# i = 1
# while i < 13:
#     i = i + 1
#     if i == 4:
#         continue
#     print(i)
#
# fruits = ["banana", "apple", "orange", '0.658', '45hjt']
# for a in 'fruits':
# print(a)

# even = [2, 4, 6]
# for correct in even:
#     print(even)

# for i in 'mango':
#     print(i)

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# for i in fruits:
#     print(i)
#     if i == 'orange':
#         break
#
# Jewelery = ['silver', 'gold', 'diamond', 'platinum']
# for q in Jewelery:
#     print(q)
#     if q == 'diamond':
#         break
#
# for abc in range(2, 10, 3):
#     print(abc)
#
# for g in range(8):
#     print(g)
# else:
#     print('done!')

# for mad in range(3, 14,5):
#     print(mad)
#
# print(mad)
#
# clothes = ['cotton', 'jeans', 'wool', 'silk']
# vehicles = ['tesla', 'honda', 'nissan', 'ford']
# for a in clothes:
#     for b in vehicles:
#         print(a, b)

# for v in [0, 5, 6, 87]:
#     pass

# def my_project():
#     print('Hi world!')
#
#
# def my_project(name):
#     print(name  + 'files')
#
# my_project('Madhu')
# my_project('Ganesh')
# my_project('Geetha')
#
# for i in range(6):
#     if i == 3 and 4:
#         continue
#     print("hello", i)
#
# #
# for i in range(5):
#     for j in range(8-i):
#         print("*  ", end="")
#
#     print()

# def my_function(*Students):
#     print("The youngest child here is", Students[-2])
#
#
# my_function("Student 1: Madhu", "Student 2: Ganesh", "Student 3: Akash")


# def my_function(Student1, Student2, Student3):
#     print("The good student here is " + Student1)
#
#
# my_function(Student1="Madhu", Student2: "Ganesh", Student3 = "Akash")


# def my_function(**kid):
#     print("His last name is " +kid["lname"])
#
# my_function(fname="mark", lname="zukerburg")

# def my_function(country = "Prague"):
#     print("I am from " + country)
#
# my_function("Sweden")
# my_function()
# my_function()
# my_function("Switzerland")

# num = 14
#
# for i in range(2, num):
#     if num % i == 0:
#         print("not prime")
#         break
#     else:
#         print("prime")

# from array import *
#
# vals = array('u', ['g', 'r', 'h', 'w', 'k'])
#
# for e in vals:
#   print(e)
#
# from array import*
#
# vals = array('i', [5, 9, 5, 3, 2])
#
# newArr = array(vals.typecode( g*g for g in vals)
# for e in newArr:
#      print(e)


# def recursion(k):
#     if k > 1:
#         result = k + recursion(k - 2)
#         print(result)
#     else:
#         result = 1
#     return result
#
#
# print("Recursion Example Results")
# recursion(6)


# def func(n):
#     return lambda a, b: a - b + n
#
#
# doubler = func(2)
#
# print(doubler(20, 10))
#
# cars = ['Toyota', 'Ford', 'Tesla', 'Mercedes']
# # print(cars[1])
# # cars[0] = 'Hyundai'
# # print(cars[0])
#
# cars.append('Volvo')
# cars.insert(2,'MG')
# print(cars)
# cars.pop(2)
# print(cars)
# print(cars.pop(1))
# print(cars)
# print(sort())
#
# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def myfunc(self):
#         print(self.firstname, self.lastname)
#
#
# class student(person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#
#     def welcome(self):
#       print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear, "batch")
#
#
# x = student("Madhu", "Kumble", "2019")
# x.welcome()

#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a = self.a + 1
#         return x
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#
# spam_amount = 0
# print(spam_amount)
#
# spam_amount = spam_amount + 4
# if spam_amount > 0:
#     print("But I don't want any spam!")
#
# viking_song = "spam " * spam_amount
# print (viking_song)
#
# print(float(56))
# print(int(48.99))
#
# print(int('807') + 1)
# a, b = 1, 2
# print(a+b-a*8/10.568)

# def test_var_args(f_arg, *argv):
#     print("first normal arg:", f_arg)
#     for arg in argv:
#         print("another arg through *argv:", arg)
#
# test_var_args('yasoob', 'python', 'eggs', 'test')

# help("modules")
# help(round(-5.08)
# print(round(-51.87))
#
# a = [1, 2, 3]
# b = [3, 2, 1]
# a,  b = b, a
# print(a)

# help(print)

# help("modules spam")


# print(abs(-79))
# print(int('10m'*2) + 1)

# print('enter your first name: ')
# firstname = input()
# print('enter your last name: ')
# lastname = input()
# print("you entered: ", firstname,lastname)

# print(help(round())

# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(c - a)
#     return min(diff1, diff2, diff3)
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
# )
#

# a = 50
# b = 100
# sum = a + b
# """the sum of a and b is: """
#
# print(sum)

# def least_difference(a, b, c):
#     """Return the smallest difference between any two numbers
#     among a, b and c.
#     """
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     min(diff1, diff2, diff3)
#
#
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7),
# )

# print("madhu", "kumble", sep=' + ')

# def lion(abc = "madhu"):
#     print("hello", abc)
#
# lion()
# lion(abc = "kaggle")
# lion(abc = "world")

# def my_func(x):
#     return 5 * x
#
# def num (fn, arg):
#     return fn(arg)
#
# def squared_num (fn, arg):
#     return  fn(fn(arg))
#
# # print (num(my_func, 1), squared_num(my_func, 1), sep = '\n',)
#
# def mod(x):
#     """Return the remainder of x after dividing by 5"""
#     return x % 5
#
# print(
#     'Which number is biggest?',
#     max(100, 51, 14),
#     'Which number is the biggest modulo 5?',
#     min(100, 51, 14, key=mod),
#     sep='\n',
# )

# num = 87.584
# print(round(num, -2))

# x = True
# print(x)
# print(type(False))
#
# def age_to_vote(age):
#     return age >= 18
#
# print("can a 18 year boy vote?", age_to_vote(18))
# print("can a 23 year boy vote?", age_to_vote(27))

# print('3.0' == "3.00")

# def is_even(num):
#     return num % 2 == 0
#
# print("is 56 even?", is_even(56))
# print("is -584 even?", is_even(-584))

# def can_run_for_president(age, citizen):
#     return citizen and (age >= 35)
#
# print("can i run for president with age 28 with citizenship?", can_run_for_president(28, True))
# print("can i run for president with age 67 without citizenship?", can_run_for_president(67, False))

# print(True or (True and False))
#
# prepared_for_weather = 'have_umbrella' \
#                        or ((rain_level < 5) and have_hood) \
#                        or (not (rain_level > 0 and is_workday))
# print(prepared_for_weather)

# def check_num(x):
#     if x == 0:
#         print(x, "is zero")
#     elif x > 0:
#         print(x, "is positive")
#     elif x < 0:
#         print(x, "is negative")
#     else:
#         print("enter either positive, negative or zero")
#
# check_num(45)
# check_num(-36.48)
# check_num(0.0)

# print(bool(''))

# if 0:
#     print(0)
# elif "spam":
#     print("spam")


# def quiz_result(grade):
#     if grade < 40:
#          print("you have failed the quiz with grade", grade, ". better luck next time")
#     else:
#         print("congratulations! you have passed the quiz with grade", grade)
#
#
# quiz_result(34)
# quiz_result(89)


# my_favourite_things = [32, 'raindrops on roses', help]
# print(my_favourite_things)


# a = 76 + 12j
# print(a.imag)


# x = 12
# print(help(x.bit_length()))

# list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list.append('g'))
# print('h' in list)
# print(list.count('abc'))

# t = (1, 2, 3)
# t[1] = 10

# x = 0.128
# print(x.as_integer_ratio())
#
# numerator, denominator = x.as_integer_ratio()
# print(numerator / denominator)
# a = 10
# b = 20
# a, b = b, a
# print('a = ', a, 'and',  'b = ', b)

# a = [5, 9, 6, 7]
# print(a.index(9))

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end=' ')

# multiplicands = (8/4, 2*9, 3.56, 4%3, 5)
# product = 1
# for num in multiplicands:
#     product = num * product
# print(product)

# s = 'maDhu iS a verY Go0D bOy'
# for char in s:
#     if char.upper():
#         print(char, end = ' ')

# for i in range (5):
#     print("the num is: ", i)

# i = 0
# while i < 10:
#     print(i, end =' ')
#     i = i+1

# squares = [n**2 for n in range(5)]
# print(squares) #with a list comprehension

# squares = []
# for n in range(6):
#     squares.append(n**2)
# print(squares)

# names_list = ['madhu', 'ganesh', 'giridhar', 'geetha', 'shashidhar', 'hari', 'krishna', 'aadi']
# short_name= [name for name in names_list if len(name) < 7]
# print(short_name)

# names_list = ['madhu', 'ganesh', 'giridhar', 'geetha', 'shashidhar', 'hari', 'krishna', 'aadi']
# caps_short_names = [name.upper() + ':)'
#     for name in names_list
#     if len(name) < 7]
# print(caps_short_names)

# string = 'ma0+4+9dhu56/'
# print(string.upper())

# c = [59 for name in names_list]
# print(c)

# nums = [2, 8, 3, -4, 5, -9]
# for neg in nums:
#     if neg < 0:
#         print(neg, end =' ')

# def count_negatives(nums):
#     # Return the number of negative numbers in the given list.
#     return sum([num for num in nums < 0])
#     count_negatives([5, -1, -2, 0, 3])
#     print(count_negatives())
    # n_negative = 0
    # for num in nums:
    #     if num < 0:
    #         n_negative = n_negative + 1
    # return n_negative


# print("hello")
# print("world")
# print("hello", end=' ')
# print("pluto", end='=')

# planet = 'Pluto'
# print([char + '!' for char in planet])

# datestr = '22 11 1997'
# date, month, year = datestr.split('-')
# print(datestr)

# datestr = '22-11-1997'
# date, month, year = datestr.join('/')
# print(date, month, year)

# planet = 'pluto'
# position = ['7', '8', '9', '10']
# print("{}, you will be the {}th planet.". format(planet, position[2]))

# planet = 'pluto'
# pluto_mass = 1.345 * 10**24
# earth_mass = 5.9782 * 10**26
# population = 56874215
#
# print("{} weighs about {:.2} kilograms ({:.2%} of earth's mass). it is home to {:,} plutonians.".format(planet, pluto_mass, pluto_mass/earth_mass, population))

# s = "pluto is a {0}!.\nAlso it's the {1}!.".format('planet', 'smllest planet')
# print(s)


# names = {'1' : 'Madhu', '2' : 'Ganesh', '3' : 'Sharma', '4' : 'Amma'}
# planet_letter = {name: name[0] for name in names}
# print(planet_letter)
# print('Madhu' in names)
# print(names['3'])

# names = {'1' : 'Madhu', '2' : 'Ganesh', '3' : 'Sharma', '4' : 'Amma'}
# for k in names:
#     print("{} = {}".format(k, names[k]))

# names = {'1' : 'M', '2' : 'G', '3' : 'S', '4' : 'A'}
# print(', '.join(sorted(names.values())))

# planet = {'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}
# for planet, initial in planet.items():
#     print('{} begins with " {} "'.format(planet.rjust(8), initial))

# def word_search(doc_list, keyword):
#     doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
#     print(word_search(doc_list, 'cad'))

# import math
# # print(help(math.log))
# print(math.log(32,5))


# from math import log, pi
# import numpy



# import numpy
# print("numpy.random is a", type(numpy.random))
# print("it contains names such as...",
#       dir(numpy.random)[-15:]
#      )

# rolls = numpy.random.randint(low =1, high = 6, size = 10)

# import numpy
# rolls = numpy.random.randint(low=1, high=6, size=10)
# x = [2, 5, 9, 6, 7]
# y = x + 10
# print(y)

# xlist = [[1, 2, 3], [4, 5, 6]]
# x = None

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is" , self.name, "and I'm", self.age, "years old.")
#
# class child(Person):
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
# x = child("Madhu", "Kumble")
# x.myfunc()

# x = ['madhu', '46', 'ganesh', '36.254']
# print(x.count('ganesh'))

# s = ['MADHU', 'Ganesh', 'amma', 'appa']

# for i in range (0, len(s)):
#     print(s[i])

# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
# def printname(person):
# xyz = person('madhu', 'kumble')
# print(xyz.firstname, xyz.lastname)

# string = "Hello world, I love Python"
# substring = "Python"
#
# if string.find(substring) is not -1:
#     print("Python found the substring")
# else:
#     print("Pythn did'nt find the substring")

# end = None
# x = "0123456789"
# print(x[0:9:2])

# txt = "hello, my name is Madhu!, and I am 26 years old"
# x = txt.split(",")
# print(x)

# s = 'My Name is Pankaj'
#
# if 'Name' in s:
#     print('Substring found')
#
# if s.find('Name') != 0:
#     print('Substring found!!')

# s = 'My Name is Pankaj'
# print('Substring count =', s.count(' '))

# s = 'abcd1234dcba'
# print(s.find('d1', 0, 2))
#
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(fox):
#     print(fox.firstname, fox.lastname)
#
# class student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduation = year
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the batch of", self.graduation)
#
# z = student("Madhu", "Kumble", 2019)
# print(z.welcome())

# class MyNumbers:
#   def __iter__(self):
#     self.a = 0
#     return self
#
#   def __next__(self):
#       if self.a <= 10:
#         x = self.a
#         self.a += 1
#         return x
#       else:
#           raise StopIteration
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)

# import datetime
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%A %B %p"))

# import json
# x = '{"name": "madhu", "age": "22", "nationality": "indian"}'
# y = json.loads(x)
# print(y['age'], "and", y['nationality'])

# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
#
# print(json.dumps(x, indent = 4, sort_keys=False))

# import re
# str = "My country is India"
# x = re.search("^My.*India$", str)
#
# print(r'G\nP')
#
# if (x):
#     print("There is a match!")
# else:
#     print("No match found.")

# import re
# text = "i'm honky but not donkey, also not monkey."
# x = re.findall("nkx+", text)
#
# print(x)
#
# if (x):
#     print("there is a match")
# else:
#     print("there is no match")

# x = "10"
#
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# f_n = input("Enter your full name:")
# print("Your full name is: ", f_n)

# price = 49
# cents = 35
# txt = "The price is {} dollars and {} cents."
# print(txt.format(price, cents))

# def main():
#     # Replace all ______ with rjust, ljust or center.
#
#     thickness = int(input())  # This must be an odd number
#     c = 'H'
#
#     # Top Cone
#     for i in range(thickness):
#         print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
#
#     # Top Pillars
#     for i in range(thickness + 1):
#         print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
#     # Middle Belt
#     for i in range((thickness + 1) // 2):
#         print((c * thickness * 5).center(thickness * 6))
#
#         # Bottom Pillars
#     for i in range(thickness + 1):
#         print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
#         # Bottom Cone
#     for i in range(thickness):
#         print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
#             thickness * 6))

# N,M = map(int,input().split())
# for i in range(1, N, 2):
#     print ( str('.|.')*i ).center(M, '-')
# print(str('WELCOME').center(M, '-'))
# for i in range(N-2, -1, -2):
#     print ( str('.|.')*i ).center(M, '-')

# class Data(object):
#
#     def __str__(self):
#         return 'madhu'
#
#     def __repr__(self):
#         return 'kumble'
# print("{0!s} {0!r}".format(Data()))
# str = "trampoline"
# print('{:.8}'.format("trampoline"))

# value1 = ord('AB')
# # prints the unicode value
# print(value1)

# def print_rangoli(n):
#
#
# # n = int(raw_input())
# for i in range(n):
#     s = "-".join(chr(ord('a') + n - j - 1) for j in range(i + 1))
# print((s + s[::-1][1:]).center(n * 4 - 3, '-'))
#
# for i in range(n - 1):
#     s = "-".join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
# print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

