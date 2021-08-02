import pytest
def word_score(word):
    """
    This function takes in a string of alphabets and returns the cumulative score
    of each of the word in the string as an integer

    INPUT - word (str) - string of alphabets

    OUTPUT - int - cumulative score of each alphabets in the string

    """

    alphabet_score = {
                       'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4,
                       'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3,
                       'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8,
                       'y':4, 'z':10
                    }


    return sum(alphabet_score[i] for i in word)
