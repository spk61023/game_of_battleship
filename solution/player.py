from board import Board


class Player:
    def __init__(self,name,grid_size,no_of_ships,missiles):
        self.name =name
        self.grid_size=grid_size
        self.no_of_ships=no_of_ships
        self.missiles=missiles
        self.board = Board(name,grid_size)
        self.hit =0
        self.miss =0
        print("PLAYER INIT COMPLETE FOR ",self.name.capitalize())

    def setup_board(self,grid_size):
        ''' setup board of player with random ship placement'''
        self.board.set_player_board(self.board,grid_size)

    def strike(self,guess_col,guess_row):
        ''' Register Hit, Miss and set value to board'''
        print("STRIKE IS IN PROGRESS")
        result = self.board.compare_ship_location(guess_col,guess_row)
        print("result",result)
        # if guess_col == self.board.board[self.board.ship_col] and guess_row == self.board.board[self.board.ship_row]:
        #     print("HIT")
        #     self.board.board[guess_col][guess_row]="X"
        #     self.hit +=1
        # else:
        #     print("MISS")
        #     self.miss +=1
        #     self.board.board[guess_col][guess_row]="O"
        print("name ",self.name," hit ",self.hit," miss ",self.miss)
        print("STRIKE COMPLETED")

    def calculate_score(self):
        '''return score of the player'''
        return self.hit

    def make_move(self,guess_col,guess_row):
        '''player enters row and col values'''
        print("Making move",guess_col,guess_row)
        self.strike(guess_col ,guess_row)




#Test
#ValueError: invalid literal for int() with base 10: '..'
#IndexError: list index out of range
