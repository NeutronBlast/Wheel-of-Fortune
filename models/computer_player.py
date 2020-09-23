import models.player as player


class ComputerPlayer(player.Player):
    def __init__(self, category, phrase, turn, name="CPU"):
        super().__init__(name, category, phrase, turn=turn)
