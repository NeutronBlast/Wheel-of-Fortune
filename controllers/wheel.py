from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import random
import time

from models import game, human_player
from controllers import wheel
from PyQt5.QtGui import QPixmap


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

        # Enabled / Disabled flags
        self.spin_state = True
        self.guess_state = False

        # Set UI
        self.word_l.setText("WORD: " + player.phrase + " " + str(len(player.phrase)) + " LETTERS")
        self.cat_l.setText("CATEGORY: " + player.category)
        self.turn_l.setText("TURN: " + player.name)
        self.balance_l.setText("BALANCE: $" + str(player.money))

        # Set buttons
        self.spin_btn.mousePressEvent = self.get_prize
        self.guess_btn.mousePressEvent = self.try_guess

    def wheel_value(self):
        random_prize = random.choice(self.wheel)
        return random_prize

    def get_prize(self, event):
        # If button is enabled
        if self.spin_state:
            self.disable_spin_enable_guess()
            self.player.prize = self.wheel_value()
            self.prize_l.setText("PRIZE: " + str(self.player.prize))

            # If player goes bankrupt loses their turn and their money
            if self.player.prize == 'bankrupt':
                self.player.go_bankrupt()
                self.computer.turn = True
                print("went bankrupt")
                self.try_guess(event)
            elif self.player.prize == 'lose a turn':
                self.player.lose_a_turn()
                self.computer.turn = True
                print("lost a  turn")
                self.try_guess(event)
        else:
            return

    def disable_spin_enable_guess(self):
        # Disable spin button and enable the guess button
        pm = QPixmap("design/spin_btn_disabled.png")
        self.spin_btn.setPixmap(pm)
        self.spin_state = False

        pm = QPixmap("design/guess_btn.png")
        self.guess_btn.setPixmap(pm)
        self.guess_state = True

    def disable_guess_enable_spin(self):
        pm = QPixmap("design/spin_btn.png")
        self.spin_btn.setPixmap(pm)
        self.spin_state = True

        pm = QPixmap("design/guess_btn_disabled.png")
        self.guess_btn.setPixmap(pm)
        self.guess_state = False

    def disable_guess_disable_spin(self):
        # If CPU'S turn
        pm = QPixmap("design/guess_btn_disabled.png")
        self.guess_btn.setPixmap(pm)
        self.guess_state = False

        pm = QPixmap("design/spin_btn_disabled.png")
        self.spin_btn.setPixmap(pm)
        self.spin_state = False

    def try_guess(self, event):
        if self.player.turn and self.guess_state:
            self.player.letter = self.guess_txt.toPlainText()

            self.player.money, self.player.turn = self.player.guess(self.word.lower())

            # If player lost turn grant turn to CPU
            if not self.player.turn:
                self.computer.turn = True
                self.disable_guess_disable_spin()
            else:
                self.disable_guess_enable_spin()

            # Set UI
            self.balance_l.setText("BALANCE: $" + str(self.player.money))
            self.word_l.setText("WORD: " + self.player.phrase + " " + str(len(self.player.phrase)) + " LETTERS")
            if len(self.player.guessed) > 0:
                self.guessed_l.setText("GUESSED: " + ", ".join(self.player.guessed))

        if self.computer.turn:
            print("CPU's turn")
            # Computer's turn
            self.computer.turn = True
            self.turn_l.setText("TURN: " + self.computer.name)

            # Only print non-empty list to avoid errors
            if len(self.computer.guessed) > 0:
                self.guessed_l.setText("GUESSED: " + ", ".join(self.computer.guessed))
            self.word_l.setText("WORD: " + self.computer.phrase + " " + str(len(self.player.phrase)) + " LETTERS")
            time.sleep(1)
            self.computer.turn = False
            print("Player's turn")
