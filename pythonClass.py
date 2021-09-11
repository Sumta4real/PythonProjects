# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:41:41 2021

@author: user
"""

"""
Class is a template for creating objects with related data and functions that 
do interesting things with that data

Classes are used to make objects and each object can have different values for  
same variable names. 
You an attach additional objects to the variable names

FEATURES OF CLASS
Methods (function inside a class) 
Object Initialization
Help text

Init method {def __init__(self,first_name)}== Initialization == Constructor (
    this method is called everytime you create a new instance of a class
    the 1st argument here is the word 'self' i.e reference to new object being created
    the self keyword is only used when writing a method
    step1: store the value to field in the objects{self.name(feild) = first_name(value)})
    'pass' in python s tellling the computer to skip the line and do no nothing 
"""

import datetime 
class User:
   """
   A member of Friendface. For now, we are only storing their names and birthday.
   But soon we will store an uncomfortable amount of user information
   """
   def __init__(self, full_name, birthday):
       self.name = full_name
       self.birthday = birthday #yyyymmdd
       
       #Extract first and last names
       name_pieces = full_name.split(' ')
       self.firstname = name_pieces[0]
       self.lastname = name_pieces[1]
       
   def age(self):
       """ Return age of the user in years"""
       today = datetime.date(2001, 5, 12)
       yyyy = int(self.birthday[0:4])
       mm = int(self.birthday[4:6])
       dd = int(self.birthday[6:8])
       dob = datetime.date(yyyy,mm,dd)
       age_in_days = (today - dob).days
       age_in_years = age_in_days/365
       return int(age_in_years)
       
   
user1 = User('Sumayyah Taiwo','19961116')
user1.age()
user1.name 
user1.firstname
user1.lastname
       

#Lambda Expression
"""
Lambda expressions are anonymous expressions. they do not have name.
lambda x(input): <expression>
You cannot use lambda expression for multiline functions
"""
#write function to compute 3x+1

#method1
def f(x):
    return 3*x + 1
f(2)

#method2
g = lambda x: 3*x + 1
g(2)

#combine first name and last name into a single 'Full name'
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
full_name('Yusroh', 'Hassan')

#sort the list using the lastname
cambio_staff = ['Shedi Didi', 'Salau Gbemi', 'Mr Lee', 'Kate Mum', 'Dr G','J JW']

#create anonymous function that extracts the lastname and uses it to sort the list
cambio_staff.sort(key= lambda name:name.split(' ')[-1].lower())
cambio_staff


#Write functions that makes functions (eg. Quadratic equations)
def build_quadratic_functions(a, b, c):
    """ Returns the function f(x) = ax^2 +bx + c"""
    return lambda x: a*x**2 + b*x + c

n = build_quadratic_functions(2, 3, -5)
n(3)


"""
Map function takes 2 argument- function to be performed; list,tuple or other 
iterable object
"""

movies = [('Gandhi', 1990), ('Star wars',1989), ('Games of throne', 2008),
          ('Citizen cane',2007),('Shawsank Redemption', 2003), 
          ('Ghost bursters', 1996),('Rare windows', 1800),('Gatacca', 2000),
          ('Gone with the wind', 2010),("It's a wonderful life",1999)]

minus1000 = [(title, year-1000 ) for (title,year) in movies]
print(minus1000)

#using maps
minus1000_a = list(map(lambda data:(data[0], data[1]-1000), movies))
minus1000_a

"""
filter function is use to select certain peices of data from a list of tuple or
other collection of data.
It takes 2 argument- function to be performed; list,tuple or other 
iterable object
"""

#get movie year greater than average
yr_ls = [year-1000 for (title,year) in movies]
year = list(filter(lambda x:x>1000, yr_ls))
year

#removing missing data
#In python, empty values are treated as False