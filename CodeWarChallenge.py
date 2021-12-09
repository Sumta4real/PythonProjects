--------------------------------Challenge 1
#Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
#[0, 0, 1, 0] is treated as 0010 which is the binary representation of 2

#### My Solution
def binary_array_to_number(arr):
    return sum([2**index*digit for index,digit in enumerate(reversed(arr))])

##Optimised Solution 
def binary_array_to_number(arr):
    return (int(''.join(map(str, arr)), 2))
  
  
--------------------------------Challenge 2
#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

#### My Solution
def find_short(s):
    return min(map(len,s.split()))

### Over Sabi Solution :: This returns the word(s) with the minimum length
def find_shortWord(s):
    return ([i for i in s.split() if len(i)== min(map(len,s.split()))])
