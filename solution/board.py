from random import randint

import numpy as np


class Board:
    def __init__(self,player_name,grid_size):
        self.board=[]
        self.ship_row = None
        self.ship_col = None
        self.player_name = player_name
        for value in range(0,grid_size):
            self.board.append([str(value+1)]*grid_size)
            print(self.board[value])
        print("BOARD INIT COMPLETE FOR ",self.player_name)

    def display_board(self,board):
        ''' X-Dead, O-Miss, B-Alive Logic'''
        print("PLAYER ",self.player_name)
        for value in board.board:
            print(" ".join(value))

    def set_player_board(self,board,no_of_ships):
        for ship in range(0,no_of_ships):
            self.ship_row = randint(0, len(self.board) - 1)
            self.ship_col = randint(0, len(self.board) - 1)
            print("self.board[self.ship_row][self.ship_col]",self.board[self.ship_row][self.ship_col])
            self.board[self.ship_row][self.ship_col] = "S"

    def confirm_all_ships(self,no_of_ships):
        '''Confirm if all no of ships are placed'''
        print("confirm_all_ships")
        generated_ships = np.array([self.board])
        count = np.count_nonzero(generated_ships == "S")
        if count != no_of_ships:
            generate_remaining_count = no_of_ships- count
            self.set_player_board(self.board,generate_remaining_count)

    def set_miss_ship(self,guess_row,guess_col):
        self.board[guess_row][guess_col]="O"

    def set_dead_ship(self,guess_row,guess_col):
        self.board[guess_row][guess_col]="X"

    def compare_ship_location(self,guess_col,guess_row):
        print("compare_ship_location")
        print("self.board[guess_col][guess_row]",self.board[guess_col][guess_row])
        print("self.board[self.ship_col][self.ship_row]",self.board[self.ship_col][self.ship_row])
        if self.board[guess_col][guess_row] == self.board[self.ship_col][self.ship_row]:
            return True
        return False


'''Create Unit Tests for cases:'''
# b1 = Board("Sam",5)
# b1.display_board(b1.board)

# b1.set_player_board(b1.board,5)
# b1.display_board(b1.board)

# b1.confirm_all_ships(5)
# b1.display_board(b1.board)

# #set O
# b1.set_miss_ship(1,1)
# #set X
# b1.set_dead_ship(2,2)
# b1.set_dead_ship(2,2) #already shot
# b1.set_dead_ship(0,0)
# b1.set_dead_ship(4,4)
# #b1.set_dead_ship(5,5) #shot outside board
# b1.set_dead_ship(3,3)
# b1.display_board(b1.board)

# print("display_board(self,board,is_game_complete=True)")
# b1.display_board(b1.board)
