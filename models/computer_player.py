import models.player as player


class ComputerPlayer(player.Player):
    def __init__(self, name, category, phrase, turn=False, guessed=[], letter="", money=0, prize=0, prizes_won=[]):
        super().__init__(name, category, money, prize, prizes_won)
        self.phrase = phrase
        # List of words that have been already guessed
        self.guessed = guessed
        # Letter player is trying to guess
        self.letter = letter.lower()
        self.turn = turn

    def __str__(self):
        return "Player Name: {}, Category: {}, Phrase: {}, Turn: {}, Guessed List: {}, Letter guessed: {}, Balance: {" \
               "}, Prize: {}, Prizes Won: {}" \
            .format(self.name, self.category, self.phrase, self.turn, self.guessed, self.letter, self.money, self.prize,
                    self.prizes_won)

# pl = HumanPlayer("Tate Langdon", "Music", "______ ____", False, ['a', 'c'], 'd', 390, 114)
# pl.guess('stupid high')
# pl.letter = "u"
# pl.guess('stupid high')
# print(pl)
