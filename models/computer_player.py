import models.player as player
import random


class ComputerPlayer(player.Player):
    sorted_frequencies = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y',
                          'p', 'b', 'v', 'k', 'j', 'q', 'x', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, category, phrase, guessed, turn, name="CPU"):
        super().__init__(name, category, phrase, guessed, turn=turn)

    # Values in abecedary but not in the guessed list
    def get_move(self):
        set_l = set(self.sorted_frequencies)
        set_g = set(self.guessed)
        set_v = set(self.vowels)

        # If not enough balance vocals can't be a possible letter
        if self.money < 250:
            result_set = list(set_l - set_g - set_v)
            if len(result_set) == 0:
                return False
                # If not enough balance and the last letter left is a vocal pass the turn
        else:
            result_set = list(set_l - set_g)
        return random.choice(result_set)
