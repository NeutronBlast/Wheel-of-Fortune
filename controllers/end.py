from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import main
import sys


class EndScreen(QDialog):
    def __init__(self, winner):
        super(EndScreen, self).__init__()
        uic.loadUi("gui/End.ui", self)
        self.winner = winner

        # Set UI
        self.winner_l.setText(self.winner.name+" has won $"+str(self.winner.money))

        # Set buttons
        self.retry_btn.mousePressEvent = self.restart_game
        self.close_btn.mousePressEvent = self.exit_game

    def restart_game(self, event):
        self.close()
        new_game = main.Menu()
        new_game.show()

    def exit_game(self, event):
        sys.exit()
