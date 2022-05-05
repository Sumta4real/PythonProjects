class Question():
    def __init__(self,text,ans):
        self.text = text
        self.answer = ans
    def write(self):
        print('question is {}, answer is {}'.format(self.text,self.answer))
        print(f"question is {self.text}, answer is {self.answer}")

if __name__ == '__main___':
    Q1 = Question("question1","True")
    print(Q1.write())
