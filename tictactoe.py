class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent a 3x3 board
        self.current_winner = None #this is made to keep track of the winner
    def print_board(self):
        #this is supposed to get the row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.joint(row) + ' |')

        @staticmethod
        def print_board_nums():
