from player import Player

GRID_SIZE   = 3
NO_OF_SHIPS = 3
MISSILES    = 4

class Game:
    def __init__(self):
        '''init with players,board,ship'''
        player1_name = input("Enter Player1 name:")
        self.player1 = Player(player1_name,GRID_SIZE,NO_OF_SHIPS,MISSILES)
        self.player1.setup_board(GRID_SIZE)
        print("\n________________________________________\n")

        player2_name = input("Enter Player2 name:")
        self.player2 = Player(player2_name,GRID_SIZE,NO_OF_SHIPS,MISSILES)
        self.player2.setup_board(GRID_SIZE)
        print("GAME INIT COMPLETE FOR 2 PLAYERS")

    def play_game(self):
        print("________________________________")
        self.player2.board.display_board(self.player2.board)
        print("\n________________________________\n")
        self.player1.board.display_board(self.player1.board)
        print("________________________________")
        for missile in range(MISSILES):
            print("\nplayer playing :",self.player1.name)
            print("\nmissile no :",missile)
            guess_col = int(input("Enter Guess Col"))
            guess_row = int(input("Enter Guess Row"))
            self.player2.make_move(guess_col,guess_row)
            print("______________________________")
            print("\nplayer playing :",self.player2.name)
            print("\nmissile no :",missile)
            guess_col = int(input("Enter Guess Col"))
            guess_row = int(input("Enter Guess Row"))
            self.player1.make_move(guess_col,guess_row)
        self.calculate_result()


    def calculate_result(self):
        '''if damage is same game is drawn,else player1 or player2 has won'''
        player1_score = self.player1.calculate_score()
        player2_score = self.player2.calculate_score()
        print("player1 HIT:",player1_score)
        print("player2 HIT:",player2_score)
        if player1_score == player2_score:
            print("GAME IS DRAWN!!")
        elif player1_score < player2_score:
            print("PLAYER 1",self.player1.name.capitalize()," WON!")
        else:
            print("PLAYER 2",self.player2.name.capitalize()," WON!")
