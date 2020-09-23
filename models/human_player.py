import models.player as p


class HumanPlayer(p.Player):
    def __init__(self, name, category, phrase, turn):
        super().__init__(name, category, phrase, turn=turn)

    # The user can type out the entire phrase, return True if the word is correct thus player wins the game
    @staticmethod
    def guess_entire_phrase(complete_word, user_word):
        if user_word.lower() == complete_word:
            return True
        else:
            return False
