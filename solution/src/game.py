from player import Player

GRID_SIZE   = 5
NO_OF_SHIPS = 5
MISSILES    = 5
WIN_THRESHOLD = 3

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
        # for missile in range(MISSILES):
        missile =0
        while missile < MISSILES:
            missile+=1
            print("\nplayer playing :",self.player1.name)
            print("\nmissile no :",missile)
            guess_row = input("Enter Guess Row")
            guess_col = input("Enter Guess Col")
            try:
                self.player2.make_move(int(guess_row),int(guess_col))
                print("______________________________")
            except Exception as e:
                print(e)
            print("\nplayer playing :",self.player2.name)
            print("\nmissile no :",missile)
            guess_row = input("Enter Guess Row")
            guess_col = input("Enter Guess Col")
            try:
                self.player1.make_move(int(guess_row),int(guess_col))
            except Exception as e:
                print(e)

            #Terminate if game is drawn
            player_1_damage, player_2_damage = self.get_players_scores()
            if player_1_damage==WIN_THRESHOLD and player_2_damage==WIN_THRESHOLD:
                print("GAME IS DRAWN!!")
                break
        self.calculate_result()
        self.display_player_boards()

    def get_players_scores(self):
        player1_score = self.player1.calculate_score()
        player2_score = self.player2.calculate_score()
        return player1_score,player2_score

    def display_player_boards(self):
        print("________________________________")
        self.player2.board.display_board(self.player2.board)
        print("\n________________________________\n")
        self.player1.board.display_board(self.player1.board)
        print("________________________________")

    def calculate_result(self):
        '''if damage is same game is drawn,else player1 or player2 has won'''
        player1_score = self.player1.calculate_score()
        player2_score = self.player2.calculate_score()
        print("player1 Damage:",player1_score)
        print("player2 Damage:",player2_score)
        if player1_score == player2_score:
            print("GAME IS DRAWN!!")
        elif player1_score < player2_score:
            print("PLAYER 1",self.player1.name.capitalize()," WON!")
        else:
            print("PLAYER 2",self.player2.name.capitalize()," WON!")
