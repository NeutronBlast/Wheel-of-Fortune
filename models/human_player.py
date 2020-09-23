import models.player as p


class HumanPlayer(p.Player):
    def __init__(self, name, category, phrase, guessed, turn):
        super().__init__(name, category, phrase, guessed, turn=turn)

    # The user can type out the entire phrase, return True if the word is correct thus player wins the game
    def guess_entire_phrase(self, complete_word, user_word):
        if user_word.lower() == complete_word:
            return True, True
        else:
            return False, False
