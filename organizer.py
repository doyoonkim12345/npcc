from konlpy.tag import Okt
import nltk

class organize:
    def __init__(self):
        self.okt = Okt()
        self.tokens = 0
        self.token = ''
        pass

    def tokenizing(self, text):
        self.tokens = self.okt.morphs(text)
        self.token = nltk.Text(self.tokens)
        return self.token

    def graghprinter(self):
        print(len(self.token))
        print(self.token)
        print(FreqDist(self.token))
        print(type(self.token))
        self.token.plot(50)
        print(type(self.token))
