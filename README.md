# Wheel of Fortune
Final project of Python Classes and Inheritance from University of Michigan, with some personal modifications for a more
user friendly playable game

## About the project
 In this game the player will play against the `Computer Player`, the user enters the name of the players,
 the program will choose a random category and a random phrase and the game starts.
 
 The player will spin the wheel and get a random prize, if they prize is `bankrupt` player loses all their money and
 the turn
 
 The player will input in a textfield the letter they think it appears in the phrase, vowels have a cost of $250, so, 
 unless the player has a balance equal or superior to that number they won't be able to input vowels. If the user inputs
 a letter that exists in the word they will gain as many money the wheel indicated multiplied for the number of occurrences
 of said word. For example
 
 **WORD:** You Gotta Fight Now
 
 **PRIZE IN WHEEL:** 500$
 
 **LETTER GUESSED**: T
 
 The number added to the balance will be: `2*500 = 1000`
 
 If the player guesses the word correctly they get to keep the turn, otherwise it will be the other player's (CPU).
 Given that the player has the advantage of guessing the whole word (which CPU hasn't), CPU doesn't have the possibility
 of going bankrupt or losing a turn in the wheel, so the game gets balanced a little bit.
 
## Built with
1. [Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html)
2. [PyQT5](https://pypi.org/project/PyQt5/)

## Resources
1. [QTDesigner](https://doc.qt.io/qt-5/qtdesigner-manual.html)
2. [PyCharm Professional](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)

## Run the project
1. Clone the repo
2. Open the project's folder in PyCharm, set the script path to `main.py`, or open PyCharm's terminal and run 
`python main.py`