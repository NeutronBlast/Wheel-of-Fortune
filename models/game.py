import random
import json


class Game:
    def __init__(self, n_humans=1, n_computers=1, word=""):
        self.n_humans = n_humans
        self.n_computers = n_computers
        self.word = word

    def __str__(self):
        return "Game has {}".format(self.word)

    # Pick a word randomly from the file
    @staticmethod
    def get_word():
        with open("./files/phrases.json", "r") as phrases:
            all_phrases = json.loads(phrases.read())
            word = random.choice(all_phrases['phrases'])
            return word

    @staticmethod
    def get_underscored_word(word):
        word_aux = ""
        for index, letter in enumerate(word):
            if letter not in ["'", " "]:
                word_aux = word_aux + "_"
            else:
                word_aux = word_aux + letter
        return word_aux

# g = Game(1, 1)
# print(g.wheel_value())
# print(type(g.wheel_value()))
