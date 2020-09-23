import models.player as p


class HumanPlayer(p.Player):
    def __init__(self, name, category, phrase, turn=True, guessed=[], letter="", money=0, prize=0, prizes_won=[]):
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

    # The user can type out the entire phrase, return True if the word is correct thus player wins the game
    @staticmethod
    def guess_entire_phrase(complete_word, user_word):
        if user_word.lower() == complete_word:
            return True
        else:
            return False

# pl = HumanPlayer("Tate Langdon", "Music", "______ ____", False, ['a', 'c'], 'd', 390, 114)
# pl.guess('stupid high')
# pl.letter = "u"
# pl.guess('stupid high')
# print(pl)
