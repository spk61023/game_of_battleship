from random import randint

import numpy as np


class Board:
    def __init__(self,player_name,grid_size):
        self.board=[]
        self.ship_row, self.ship_col = None,None
        self.player_name = player_name
        for value in range(0,grid_size):
            self.board.append([str(value+1)]*grid_size)
            # print(self.board[value])
        print("BOARD INIT COMPLETE FOR ",self.player_name)

    def display_board(self,board):
        ''' X-Dead, O-Miss, B-Alive Logic'''
        # print("PLAYER ",self.player_name)
        for value in board.board:
            print(" ".join(value))

    def set_player_board(self,board,no_of_ships):
        for ship in range(0,no_of_ships):
            self.ship_row = randint(0, len(self.board) - 1)
            self.ship_col = randint(0, len(self.board) - 1)
            # print("self.board[self.ship_row][self.ship_col]",self.board[self.ship_row][self.ship_col])
            self.board[self.ship_row][self.ship_col] = "S"

    def confirm_all_ships(self,no_of_ships):
        '''Confirm if all no of ships are placed'''
        generated_ships = np.array([self.board])
        count = np.count_nonzero(generated_ships == "S")
        if count != no_of_ships:
            generate_remaining_count = no_of_ships- count
            self.set_player_board(self.board,generate_remaining_count)
        generated_ships = np.array([self.board])
        return np.count_nonzero(np.array([self.board]) == "S")

    def set_miss_ship(self,guess_row,guess_col):
        self.board[guess_row][guess_col]="O"
        return self.board

    def set_dead_ship(self,guess_row,guess_col):
        self.board[guess_row][guess_col]="X"
        return self.board

    def compare_ship_location(self,guess_row,guess_col):
        if self.board[guess_row][guess_col] == self.board[self.ship_row][self.ship_col]:
            return True
        return False
