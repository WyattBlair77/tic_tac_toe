class Board:
    def __init__(self, state):
        self.state = state
        self.initial_state = [[None, None, None], [None, None, None], [None, None, None]]

    def print_board(self):
        print(" |  0  ||  1  ||  2 |    ")
        print("---------------------------------------")
        for i, count in zip(self.state, [0, 1, 2]):
            print(count, end='')
            for j in i:
                if j is None:
                    print("| ", " ", " |", end='')
                else:
                    print("| ", j, " |", end='')
            print()
            print("---------------------------------------")

    def check_end(self):
        for i in range(3):
            if (self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2]) \
                    and (self.state[i][0] is not None) and (self.state[i][1] is not None) and (self.state[i][2] is not None):
                return True
            elif self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2] \
                    and (self.state[0][0] is not None) and (self.state[1][1] is not None) and (self.state[2][2] is not None):
                return True
            elif self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0] \
                    and (self.state[0][2] is not None) and (self.state[1][1] is not None) and (self.state[2][0] is not None):
                return True
            elif self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i] \
                    and (self.state[0][i] is not None) and (self.state[1][i] is not None) and (self.state[2][i] is not None):

                return True

        return False

    def game_loop(self):
        print("TIC TAC TOE:")
        self.print_board()
        turn = -1
        prev_moves = []
        replay = True

        while not self.check_end() and replay:

            if len(prev_moves) == 9:
                turn = 0
                break

            row_move = input('Enter row you want to play in: ')
            col_move = input('Enter col you want to play in: ')

            while not (row_move.isnumeric() or col_move.isnumeric()):
                print('Invalid move. Must enter an integer for row/col.')
                print()
                row_move = input('Enter row you want to play in: ')
                col_move = input('Enter col you want to play in: ')

            row_move = int(row_move)
            col_move = int(col_move)

            while row_move > 2 or col_move > 2:
                print('Invalid move.')
                print()
                row_move = int(input('Enter row you want to play in: '))
                col_move = int(input('Enter col you want to play in: '))

            move = [row_move, col_move]
            while move in prev_moves:
                print('Invalid move. Space already occupied')
                print()
                row_move = int(input('Enter row you want to play in: '))
                col_move = int(input('Enter col you want to play in: '))
                move = [row_move, col_move]

            prev_moves += [move]

            new_state = self.state
            if turn == -1:
                new_state[row_move][col_move] = 'X'
            elif turn == 1:
                new_state[row_move][col_move] = 'O'

            self.state = new_state
            print('\n\n\n')
            self.print_board()


            turn *= -1

        if turn == 1:
            print('X WINS!!!!!')
        elif turn == -1:
            print('O WINS!!!!!')
        elif turn == 0:
            print("IT'S A TIE!!!! EVERYONE'S A LOSER :D")



