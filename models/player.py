class Player:
    def __init__(self, name, category, phrase, guessed, letter="", money=0, prize=0,
                 prizes_won=[], turn=False, winner=False):
        self.name = name
        self.category = category
        self.phrase = phrase
        self.guessed = guessed
        self.letter = letter.lower()
        self.money = money
        self.prize = prize
        self.prizes_won = prizes_won
        self.turn = turn
        self.winner = winner

    def __str__(self):
        return "Player Name: {}, Category: {}, Phrase: {}, Turn: {}, Guessed List: {}, Letter guessed: {}, Balance: {" \
               "}, Prize: {}, Prizes Won: {}" \
            .format(self.name, self.category, self.phrase, self.turn, self.guessed, self.letter, self.money, self.prize,
                    self.prizes_won)

    def lose_a_turn(self):
        self.turn = False

    def go_bankrupt(self):
        self.turn = False
        self.money = 0

    def replace_underscores(self, complete_word):
        for index, letter in enumerate(complete_word):
            if letter.lower() == self.letter:
                self.phrase = self.phrase[:index] + letter + self.phrase[index + 1:]

    def guess(self, complete_word):
        m = self.money
        guessed = False

        if self.letter.lower() in complete_word:
            # Occurrences of letter in word
            times = complete_word.count(self.letter)

            # Vowels cost 250
            if self.letter not in ['a', 'e', 'i', 'o', 'u']:
                m = (self.prize * times) + self.money
            else:
                m = (self.prize * times) - 250 + self.money

            # Replace underscores
            self.replace_underscores(complete_word.lower())
            # Add to prizes
            self.prizes_won.append(self.prize)
            guessed = True

        else:
            self.turn = not self.turn

        self.guessed.append(self.letter)
        return m, guessed
