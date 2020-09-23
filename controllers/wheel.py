from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import random
from controllers import end
from PyQt5.QtGui import QPixmap


class Wheel(QDialog):
    wheel = ['lose a turn', 120, 300, 180, 1000, 50, 500, 300, 250, 400, 800, 1200, 950, 2500, 900,
             700, 600, 650, 900, 'bankrupt']

    wheel_cpu = [120, 300, 180, 1000, 50, 500, 300, 250, 400, 800, 1200, 950, 2500, 900, 700, 600, 650, 900]

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
           , 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']

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
        self.word_l.setText("WORD: " + player.phrase + " (" + str(len(player.phrase)) + " LETTERS)")
        self.cat_l.setText("CATEGORY: " + player.category)
        self.turn_l.setText("TURN: " + player.name)
        self.balance_l.setText("BALANCE: $" + str(player.money))
        self.balance_l_cpu.setText("BALANCE: $" + str(computer.money))
        self.letter_error_msg.setHidden(True)

        # Set buttons
        self.spin_btn.mousePressEvent = self.get_prize
        self.guess_btn.mousePressEvent = self.validate_input

    def cpu_wheel_value(self):
        random_prize = random.choice(self.wheel_cpu)
        return random_prize

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

    def validate_input(self, event):
        valid = True
        # Invalid letter
        if not self.phrase_checkbox.isChecked():
            if self.guess_txt.toPlainText().lower() not in self.abc:
                valid = False
                self.letter_error_msg.setText("Please enter a valid letter")

            # Not enough balance
            if self.player.money < 250 and self.guess_txt.toPlainText().lower() in self.vowels:
                valid = False
                self.letter_error_msg.setText("You don't have enough balance to guess a vowel")

            if self.guess_txt.toPlainText().lower() in self.player.guessed:
                valid = False
                self.letter_error_msg.setText("This letter has been already guessed!")

        if valid:
            self.letter_error_msg.setHidden(True)
            self.try_guess(event)
        else:
            self.letter_error_msg.setHidden(False)

    def try_guess(self, event):
        # Don't try to guess the whole phrase
        if not self.phrase_checkbox.isChecked():
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
                hits = len([item for item in self.player.guessed if item in self.word])
                self.hits_l.setText("HITS (PLAYER): " + str(hits))
                self.word_l.setText("WORD: " + self.player.phrase + " (" + str(len(self.player.phrase)) + " LETTERS)")
                if len(self.player.guessed) > 0:
                    self.guessed_l.setText("GUESSED: " + ", ".join(self.player.guessed))

        else:
            if self.player.turn and self.guess_state:
                self.player.letter = self.guess_txt.toPlainText()
                self.player.winner, self.player.turn = self.player.guess_entire_phrase(self.word.lower(),
                                                                                       self.player.letter)

        if self.computer.turn:
            # Computer's turn
            self.turn_l.setText("TURN: " + self.computer.name)

            while self.computer.turn:
                # print(self.computer)

                # Only print non-empty list to avoid errors
                if len(self.computer.guessed) > 0:
                    hits = len([item for item in self.computer.guessed if item in self.word])
                    self.hits_l_cpu.setText("HITS (CPU): " + str(hits))

                # Set UI
                self.balance_l_cpu.setText("BALANCE: $" + str(self.computer.money))

                # Set computer's move
                self.computer.prize = self.cpu_wheel_value()
                self.computer.letter = self.computer.get_move()
                self.computer.money, self.computer.turn = self.computer.guess(self.word.lower())

            if not self.computer.turn:
                self.player.turn = True
                self.disable_guess_enable_spin()

        # If no more letters left to guess or user guesses the complete word user wins
        if self.player.winner or self.player.phrase.lower() == self.word.lower():
            self.close()
            end_game_screen = end.EndScreen(self.player)
            end_game_screen.exec_()

        if self.computer.winner or self.computer.phrase.lower() == self.word.lower():
            self.close()
            end_game_screen = end.EndScreen(self.computer)
            end_game_screen.exec_()
