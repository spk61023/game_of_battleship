Instructions to get the solution up and running

make sure you have python installed on your system

start virtual env:

    -else create and activate python -m venv

    -source /venv/Scripts/activate

    - install packages from requirements.txt

    - pip -r requirements.txt install

Solution/src directory contains battleship Game

    -battleship.py is main file which will initialize game
    -game has methods to initialize complete player and board data using other classes such as player and board

__________________________________________________________________________________________

Assumptions:

    -Battleship is a 2 player game
    -Player 1 & 2 : Enters name
    -Game will initialize the board with same values for both players
    -Next player1 &2 allocate ships randomly [this is implemented]
    -damage score is set to HIT = 0
    -player who incur max hit lose the game
    -player who has max ships alive wins the game
    -players can draw the game when there's equal no of damage dealt to each other

__________________________________________________________________________________________

Sample Execution:

    -navigate to game_of_battleship/solution/src
    '''
        $ python battle_ship.py

        ***********************
        Welcome to Battleships!
        ***********************

        Enter Player1 name:1
        BOARD INIT COMPLETE FOR  1
        PLAYER INIT COMPLETE FOR  1

        ________________________________________

        Enter Player2 name:2
        BOARD INIT COMPLETE FOR  2
        PLAYER INIT COMPLETE FOR  2
        GAME INIT COMPLETE FOR 2 PLAYERS

        player playing : 1

        missile no : 1
        Enter Guess Row1
        Enter Guess Col1
        Making move 1 1
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  2  hit  0  miss  1
        STRIKE COMPLETED
        ______________________________

        player playing : 2

        missile no : 1
        Enter Guess Row2
        Enter Guess Col2
        Making move 2 2
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  1  hit  0  miss  1
        STRIKE COMPLETED

        player playing : 1

        missile no : 2
        Enter Guess Row1
        Enter Guess Col1
        Making move 1 1
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  2  hit  0  miss  2
        STRIKE COMPLETED
        ______________________________

        player playing : 2

        missile no : 2
        Enter Guess Row0
        Enter Guess Col0
        Making move 0 0
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  1  hit  0  miss  2
        STRIKE COMPLETED

        player playing : 1

        missile no : 3
        Enter Guess Row3
        Enter Guess Col1
        Making move 3 1
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  2  hit  0  miss  3
        STRIKE COMPLETED
        ______________________________

        player playing : 2

        missile no : 3
        Enter Guess Row1
        Enter Guess Col3
        Making move 1 3
        STRIKE IS IN PROGRESS
        result True
        HIT
        name  1  hit  1  miss  2
        STRIKE COMPLETED

        player playing : 1

        missile no : 4
        Enter Guess Row4
        Enter Guess Col4
        Making move 4 4
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  2  hit  0  miss  4
        STRIKE COMPLETED
        ______________________________

        player playing : 2

        missile no : 4
        Enter Guess Row2
        Enter Guess Col0
        Making move 2 0
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  1  hit  1  miss  3
        STRIKE COMPLETED

        player playing : 1

        missile no : 5
        Enter Guess Row0
        Enter Guess Col0
        Making move 0 0
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  2  hit  0  miss  5
        STRIKE COMPLETED
        ______________________________

        player playing : 2

        missile no : 5
        Enter Guess Row3
        Enter Guess Col3
        Making move 3 3
        STRIKE IS IN PROGRESS
        result False
        MISS
        name  1  hit  1  miss  4
        STRIKE COMPLETED
        player1 Damage: 1
        player2 Damage: 0
        PLAYER 2 2  WON!
        ________________________________
        O 1 1 1 1
        S O 2 S 2
        3 3 3 3 3
        S O 4 S 4
        S 5 5 5 O

        ________________________________

        O 1 1 1 S
        2 S 2 X 2
        O 3 O 3 S
        4 4 4 O 4
        S 5 5 5 5
        ________________________________
    '''