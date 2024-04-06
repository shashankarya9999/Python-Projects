import random

print('Welcome to the game of Tic Tac Toe\n')

# function that prints out a 3x3 board. 

def display_board(board):

    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

print("The following is the indexing method. Input accordingly!\n")

placeholder_board = ['#','1','2','3','4','5','6','7','8','9']
display_board(placeholder_board)

print('\n')

# function that can take in a player input and assign their marker as 'X' or 'O'

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ').upper()

    player1 = marker
    player2 = ''

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board

def place_marker(board,marker,position):

    board[position] = marker

# function that takes in a board list object and checks if someone has won

def win_check(board,mark):

    return((board[1] == mark and board[2] == mark and board[3] == mark ) or     #row
    (board[4] == mark and board[5] == mark and board[6] == mark ) or            #row
    (board[7] == mark and board[8] == mark and board[9] == mark ) or            #row
    (board[1] == mark and board[4] == mark and board[7] == mark ) or            #column
    (board[2] == mark and board[5] == mark and board[8] == mark ) or            #column
    (board[3] == mark and board[6] == mark and board[9] == mark ) or            #column
    (board[1] == mark and board[5] == mark and board[9] == mark ) or            #diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark ))              #diagonal

# function that uses the random module to randomly decide which player goes first

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# function that returns a boolean indicating whether a space on the board is freely available

def space_check(test_board,position):

    return test_board[position] == ' '

# function that checks if the board is full and returns a boolean value. True if full, False otherwise

def full_board_check(test_board):
    for i in range(1,10):
        if space_check(test_board,i) == True:
            return False
    return True

# function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position.
# if it is, then return the position for later use

def player_choice(test_board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(test_board,position):
        position = int(input('Choose a position (1-9): '))

    return position

# function that asks the player if they want to play again and returns a boolean True if they do want to play again

def replay():

    choice = input("Play Again? Enter Yes or No: ").lower()
    return choice == 'yes'

# function that maintains a leaderboard

def leaderboard(player1_count,player2_count):
    
    print('Current Leaderboard!')
    print("Player1's score: {}".format(player1_count))
    print("Player2's score: {}".format(player2_count))
    print("\n")

# actual game logic

player1_count = 0
player2_count = 0

while True:

    the_board = [' ']*10
    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to Play? y or n: ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            # show the board    
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!\n')
                game_on = False
                player1_count += 1

            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            # show the board    
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player2_marker,position)
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!\n')
                game_on = False
                player2_count += 1

            else:
                if full_board_check(the_board) == True:
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
                else:
                    turn = 'Player 1'
    
    # leaderboard
    leaderboard(player1_count,player2_count)    

    if not replay():
        break
