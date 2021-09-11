import pytest

#creating unit test for the ScrabbleWordScoreGenerator
from ScrabbleWordScoreGenerator import word_score
@pytest.mark.scrabble
def test_scrabbleScore():
    assert word_score('star') == 4
    assert word_score('quixotic') == 26
    assert word_score('maximize') == 28
    assert word_score('jezebel') == 25
    assert word_score('quizzify') == 41
    assert word_score('fortune') == 10


#create unit test for the password_generator function
from paasword_generator import password_generator
@pytest.mark.password_generator
def test_passwordgenerator():
    assert len(password_generator(8)) == 8 , "password length not equal to the specified length"
    assert password_generator(6)
    
    
from paasword_generator import password_generator
