import random
from covers.Covers import get_cover
import requests

class Quiz:
    kart = ""
    answers = []
    coransw = ""
    def __init__ (self):
        self.answers = []
        self.cover()
        self.answ()
        self.shuffle()
    def cover(self):
        cover = get_cover()
        self.kart = cover['img']
        self.answers.append(cover['name'])
        self.coransw = cover['name']
    def answ(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        self.answers.append(random.choice(WORDS).decode())
        self.answers.append(random.choice(WORDS).decode())
        self.answers.append(random.choice(WORDS).decode())
    def shuffle(self):
        random.shuffle(self.answers)
    def check(self, msg):
        return self.coransw == msg



