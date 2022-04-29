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
        self.board.confirm_all_ships(self.no_of_ships)

    def strike(self,guess_row,guess_col):
        ''' Register Hit, Miss and set value to board'''
        print("STRIKE IS IN PROGRESS")
        try:
            result = self.board.compare_ship_location(guess_row,guess_col)
            print("result",result)
            if result:
                print("HIT")
                self.board.board[guess_row][guess_col]="X"
                self.hit +=1
            else:
                print("MISS")
                self.miss +=1
                self.board.board[guess_row][guess_col]="O"
        except Exception as e:
            print(e)
        print("name ",self.name," hit ",self.hit," miss ",self.miss)
        print("STRIKE COMPLETED")

    def calculate_score(self):
        '''return score of the player'''
        return self.hit

    def make_move(self,guess_row,guess_col):
        '''player enters row and col values'''
        print("Making move",guess_row,guess_col)
        self.missiles -=1
        self.strike(guess_row,guess_col)
