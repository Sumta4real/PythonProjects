# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#List Comprehensions
"""
[expr for val in collection]
[expr for val in colletion if <test>]
[expr for val in colection if <test1> and <test2>]
[expr for val1 in collection1 for val2 in collection2]
"""

#get the square of the first 100 integers
squares = [i**2 for i in range(0,101)]

#list of remainders when you divide the square of first 100 numbers by 5(perfectsquares mod5)
remainders5 = [i**2 % 5 for  i in range(0,101)]

#list of remainders when you divide the square of first 100 numbers by 11(perfectsquares mod11)
remainders11 = [i**2% 11 for i in range(0,101) ]

#list of movies starting with g
movies = ['Gandhi', 'Star wars', 'Games of throne', 'Citizen cane',
          'Shawsank Redemption', 'Ghost bursters', 'Rare windows', 
          'Gone with the wind','It"s a wonderful life','Gatacca']
gmovies = [title for title in movies if title.startswith('G')]
print(gmovies)

#list of movies released before the year 2000
movies = [('Gandhi', 1990), ('Star wars',1989), ('Games of throne', 2008),
          ('Citizen cane',2007),('Shawsank Redemption', 2003), 
          ('Ghost bursters', 1996),('Rare windows', 1800),('Gatacca', 2000),
          ('Gone with the wind', 2010),("It's a wonderful life",1999)]

movies_b42k = [title for (title,year) in movies if year < 2000]
print(movies_b42k)

#scalar multipication
v = [2,-9, 18]
mult = [4*x for x in v]
print(mult)

#Cartesian Product using list comprehension
"""
If A and B are sets, then the Cartesian Product is the set of the pairs(a,b)
where 'a' is in A and 'b' is in B
A x B = {(a,b) | a E A, b E b}
A = [1,3] ; B = [x,y]
A x B = {(1,x), (1,y), (3,x), (3,y)}
"""

A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


def Import_csv(file_path):
    """
    This function imports csv file
    
    input- (str)
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

#data = Import_csv()


print('Amoke Taiwo is a babe')

a = 'Allah'
r = 'rosul'
s = 'solah'
z = 'zakah'
q = 'qiblah'


import matplotlib.pyplot as plt
a = [1,2,3,4,5]
b = [2,4,6,8,10]

plt.plot(a,b)
plt.show()

