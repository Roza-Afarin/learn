import random

class BingoGame:

    players = []

    def __init__(self):
        self.name = input('Please enter your name: ')
        self.__rand_num = random.randint(0,10)
        self.__guess_left = 3
        self.__win_state = False
        self.players.append(self)

    def check_ansewr(self):
        if self.has_guess_left():
            ansewr = int(input(f'{self.name} enter your guess: '))
            if ansewr > self.__rand_num:
                print('guess lower')
            elif ansewr < self.__rand_num:
                print('guess higher')
            elif ansewr == self.__rand_num:
                print('bingo')
                self.__win_state = True
            self.__win_guess_left()
            print(f'{self.__guess_left} has left')
        

    def __win_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(player.has_won is True for player in cls.players):
            return True
        return False

class GameController:
    def __init__(self):
        while True:
            for player in BingoGame.players:
                if not player.has_won():
                    player.check_ansewr()
            if BingoGame.game_has_winner():
                break
        
if __name__ == '__main__':
    while True:
        order = input("enter your order: 'add' to add player,'start' to start game and exit  ")
        if order == 'add':
            BingoGame()
        elif order == 'start':
            GameController()
        elif order == 'exit':
            break


        