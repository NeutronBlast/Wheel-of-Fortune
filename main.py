import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from models import game
from controllers import wheel
import models.human_player as human
import models.computer_player as computer
from PyQt5.QtGui import QIcon


class Menu(QMainWindow):
    new_game = None
    human_player = None

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/Menu.ui", self)
        # Define button events
        self.start_btn.mousePressEvent = self.enable_wheel

    def enable_wheel(self, event):
        # Set new game
        self.new_game = game.Game(1, 1)
        self.new_game.word = self.new_game.get_word()
        # Get underscored word
        underscored = self.new_game.get_underscored_word(self.new_game.word['word'])
        # Set human player
        human_player = human.HumanPlayer(self.player_name.toPlainText(), self.new_game.word['category'],
                                         underscored)

        # Set computer player
        computer_player = computer.ComputerPlayer(self.computer_name.toPlainText(), self.new_game.word['category'],
                                                  underscored)
        # New window
        self.close()
        print(self.new_game.word['word'])
        wheel_wn = wheel.Wheel(self.new_game.word['word'], human_player, computer_player)
        wheel_wn.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Menu()
    GUI.show()
    app.exec_()
