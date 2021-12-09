##### Get The Middlle Character
#You are going to be given a word.
#Your job is to return the middle character of the word. If the word's length is odd, return the middle character.
#########If the word's length is even, return the middle 2 characters.

#### My Solution
def get_middle(s):
    if len(s)%2 != 0:
        return s[int(len(s)/2)]
    else:
        return s[int(len(s)/2-1):int(len(s)/2+1)]
      
### Optimised Solution
def get_middle(s):
  return s[int((len(s)-1)/2):int(len(s)/2+1)]


### Test from CodeWar Kata 
test.describe("Basic tests")
test.assert_equals(get_middle("test"),"es")
test.assert_equals(get_middle("testing"),"t")
test.assert_equals(get_middle("middle"),"dd")
test.assert_equals(get_middle("A"),"A")
test.assert_equals(get_middle("of"),"of")

test.describe("Random tests")
from random import randint
get_sol=lambda s: s[(len(s)-1)//2:len(s)//2+1]
base="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(40):
  s="".join([base[randint(0,len(base)-1)] for qu in range(randint(2,20))])
  test.it("Testing for %s" %s)
  test.assert_equals(get_middle(s),get_sol(s),"It should work for random inputs too")
