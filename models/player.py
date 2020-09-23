class Player:
    def __init__(self, name, category, money=0, prize=0, prizes_won=[], winner=False):
        self.name = name
        self.money = money
        self.prize = prize
        self.prizes_won = prizes_won
        self.category = category
        self.winner = winner

    def go_bankrupt(self):
        self.money = 0

    def replace_underscores(self, complete_word):
        for index, letter in enumerate(complete_word):
            if letter.lower() == self.letter:
                self.phrase = self.phrase[:index] + letter + self.phrase[index + 1:]

    def guess(self, complete_word):
        m = None
        if self.letter.lower() in complete_word:
            # Occurrences of letter in word
            times = complete_word.count(self.letter)
            m = (self.prize * times) + self.money

            # Replace underscores
            self.replace_underscores(complete_word.lower())
            # Add to prizes
            self.prizes_won.append(self.prize)

        else:
            self.turn = not self.turn

        # Vowels cost $250
        if self.money >= 250 and len(self.letter) > 0 and self.letter in ['a', 'e', 'i', 'o', 'u']:
            m = self.money - 250

        self.guessed.append(self.letter)
        return m
