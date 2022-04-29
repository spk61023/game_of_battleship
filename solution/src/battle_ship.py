from game import Game


class BattleShip:
    def __init__(self):
        print("\n\n***********************")
        print("Welcome to Battleships!")
        print("***********************\n")
        game = Game()
        game.play_game()


if __name__ == '__main__':
    playbattleships = BattleShip()
