from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import random
import time
from models import game, human_player
from controllers import wheel
from PyQt5.QtGui import QIcon


class Wheel(QDialog):
    wheel = ['lose a turn', 120, 300, 180, 1000, 50, 500, 300, 250, 400, 800, 1200, 950, 2500, 900,
             700, 600, 650, 900, 'bankrupt']

    def __init__(self, word, player, computer):
        super(Wheel, self).__init__()
        uic.loadUi("gui/Wheel.ui", self)
        # Set variables
        self.word = word
        self.player = player
        self.computer = computer

        # Set UI
        self.word_l.setText("WORD: " + player.phrase + " " + str(len(player.phrase)) + " LETTERS")
        self.cat_l.setText("CATEGORY: " + player.category)
        self.turn_l.setText("TURN: " + player.name)

        # Set buttons
        self.spin_btn.mousePressEvent = self.get_prize
        self.guess_btn.mousePressEvent = self.try_guess
        print(player)

    def wheel_value(self):
        random_prize = random.choice(self.wheel)
        return random_prize

    def get_prize(self, event):
        self.player.prize = self.wheel_value()
        self.prize_l.setText("PRIZE: " + str(self.player.prize))

    def try_guess(self, event):
        self.player.letter = self.guess_txt.toPlainText()
        self.player.money = self.player.guess(self.word.lower())
        self.word_l.setText("WORD: "+self.player.phrase+" "+str(len(self.player.phrase))+" LETTERS")
        self.guessed_l.setText("GUESSED: "+", ".join(self.player.guessed))

        if not self.player.turn:
            print("CPU's turn")
            self.computer.turn = True
            self.turn_l.setText("TURN: " + self.computer.name)
            self.guessed_l.setText("GUESSED: " + ", ".join(self.computer.guessed))
            self.word_l.setText("WORD: " + self.computer.phrase + " " + str(len(self.player.phrase)) + " LETTERS")
            time.sleep(1)
            self.computer.turn = False
            print("Player's turn")

