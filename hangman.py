class Hangman:
    def __init__(self, word):
        self.word = word
        self.life = 3
        self.status = True
        self.rightGuesses = []
        self.wordBlank = []
        self.head = ''
        self.torso = ''
        self.legs = ''

    def display(self):
        print('-------')
        print('|    '+self.head)
        print('|    '+self.torso)
        print('|    '+self.legs)
        for letter in list(self.word):
            if letter in self.rightGuesses:
                self.wordBlank.append(letter)
            else:
                self.wordBlank.append('-')
        print(self.wordBlank)
        

    def move(self):
        move = input('enter a letter or guess a word: ')
        return move

    def moveHandler(self, move):
        if move in list(self.word):
            self.rightGuesses.append(move)
        if move == self.word:
            self.win()
        if move not in list(self.word) and move != self.word:
            self.life -= 1

    def wordHandler(self, move):
        pass

    def win(self):
        print('you win')
        self.status = False

    def checkLoose(self):
        if self.life == 2:
            self.head = ' o '
        if self.life == 1:
            self.torso = '/|\ '
        if self.life == 0:
            self.legs = '/ \ '
            self.display()
            print('you lost')
            self.status = False

    def checkWin(self):
        if ''.join(self.wordBlank) == self.word:
            self.win()

word = input("Enter word:")

game = Hangman(word)
while game.status:
    game.wordBlank = []
    game.display()
    move = game.move()
    game.moveHandler(move)
    game.checkLoose()
    game.checkWin()
    