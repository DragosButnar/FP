from board import game_board


class skynet_level_1():
    def __init__(self, board):
        self.__board = board

    def computer_move(self):
        """
        Determine where the computer plays and make the move
        :param self:
        :return: The position where computer moved
        """
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if self.__board.get_position(row, col) is None:
                    self.__board.move('O', row, col)
                    return row, col
class game:
    def __init__(self, board: game_board, computer_player):
        self.__board = board
        self.computer_player

    def human_move(self, row, col):
        """
        Record the human's move on the board
        :param self:
        :param row:
        :param col:
        :return:
        """
        self.__board.move('X', row, col)


