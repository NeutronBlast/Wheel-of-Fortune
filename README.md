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
 
 If the player guesses the word correctly they get to keep the turn, otherwise it will be the other player's (CPU) turn