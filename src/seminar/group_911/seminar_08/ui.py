from board import game_board
from game import game, skynet_level_1


def start_game():
    board = game_board()
    computer_player = skynet_level_1(board)
    gmae = game(board)
    humans_turn = True

    while True:
        print(str(board))

        if humans_turn:
            user_input = input(">")
            command, params = user_input.split(" ", maxsplit=1)
            if command == 'play':
                params = params.split(",")
                try:
                    row = int(params[0])
                    col = int(params[1])
                    game.human_move(row, col)
                except ValueError as ve:
                    # TODO Allow user to attempt to make a move
                    print(ve)
            elif command == 'takeback':
                # Take back human's last move, if possible
                pass
            elif command == 'ragequit':
                print("Computer wins!")
                return
            else:
                print("Invalid command")
        else:
            # Computer player's turn
            row, col = game.computer_move()
            print("Computer moved at (" + str(row) + "," + str(col) + ")")
        humans_turn = not humans_turn


start_game()
