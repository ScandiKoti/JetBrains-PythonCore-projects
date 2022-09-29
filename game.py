class PuzzleBoard:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cell_size = len(str(self.row * self.column))
        self.grid = [['_' * self.cell_size for _ in range(column)] for _ in range(row)]
        self.possible_moves = [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]]
        self.temp_possible_moves = []

    def __str__(self):
        board = ' ' + '-' * (self.column * (self.cell_size + 1) + 3) + '\n'
        for i in range(self.row, 0, -1):
            board += f'{i}| {" ".join(self.grid[i - 1])} |\n'
        board += ' ' + '-' * (self.column * (self.cell_size + 1) + 3) + '\n'
        board += ' ' * 3 + " ".join((" " * (self.cell_size - len(str(x))) + str(x + 1)) for x in range(self.column)) \
                 + '\n'
        return board

    def set_position(self, position_row, position_column):
        for i in range(self.row):
            for j in range(self.column):
                if self.check_visited(i, j):
                    self.grid[i][j] = ' ' * (self.cell_size - 1) + '*'
                else:
                    self.grid[i][j] = '_' * self.cell_size
        self.grid[position_column - 1][position_row - 1] = ' ' * (self.cell_size - 1) + 'X'

    def set_possible_moves(self, pos_row, pos_column, board_width, board_height):
        for move in self.possible_moves:
            move_row, move_column = move
            if 0 <= (pos_column - 1 + move_column) < board_width and 0 <= (pos_row - 1 + move_row) < board_height and \
                    not self.check_visited((pos_column - 1 + move_column), (pos_row - 1 + move_row)):
                move_column, move_row = (pos_column - 1 + move_column), (pos_row - 1 + move_row)
                self.temp_possible_moves.append([move_row + 1, move_column + 1])
                counter = PuzzleBoard.possible_moves_counter(self, move_row, move_column, board_width, board_height)
                self.grid[move_column][move_row] = ' ' * (self.cell_size - 1) + str(counter)

    def check_visited(self, x, y):
        if self.grid[x][y] in [' ' * (self.cell_size - 1) + 'X', ' ' * (self.cell_size - 1) + '*']:
            return True
        return False

    def possible_moves_counter(self, move_row, move_column, board_width, board_height):
        counter = -1
        for next_move in self.possible_moves:
            next_move_row, next_move_column = next_move
            if 0 <= (move_column + next_move_column) < board_width and 0 <= (
                    move_row + next_move_row) < board_height:
                counter += 1
        return counter

    def check_position(self):
        while True:
            state = input("Enter your next move: ").split()
            try:
                state = [int(i) for i in state]
                position_row = state[0]
                position_column = state[1]
                if len(state) != 2:
                    raise ValueError
                elif list(state) not in self.temp_possible_moves:
                    raise IndexError
            except (ValueError, IndexError):
                print("Invalid move!")
                continue
            break
        self.temp_possible_moves = []
        return position_row, position_column

    def finish(self):
        if not self.temp_possible_moves:
            counter = 0
            for i in range(self.row):
                for j in range(self.column):
                    if self.check_visited(i, j):
                        counter += 1
            if counter == self.row * self.column:
                print('What a great tour! Congratulations!')
                exit()
            print(f'No more possible moves!/nYour knight visited {counter} squares!')
            exit()


def check_input_position(board_width, board_height):
    while True:
        state = input("Enter the knight's starting position: ").split()
        try:
            position_row = int(state[0])
            position_column = int(state[1])
            first_move = False
            if len(state) != 2:
                raise ValueError
            elif not (0 < position_column <= board_width and 0 < position_row <= board_height):
                raise IndexError
        except (ValueError, IndexError):
            print("Invalid position!")
            continue
        break
    return position_row, position_column, first_move


def check_board_dimensions():
    while True:
        board_dimensions = input("Enter your board dimensions:").split()
        try:
            board_width = int(board_dimensions[1])
            board_height = int(board_dimensions[0])
            if len(board_dimensions) != 2:
                raise ValueError
            elif not (board_width > 0 and board_height > 0):
                raise IndexError
        except (ValueError, IndexError):
            print("Invalid dimensions!")
            continue
        break
    return board_width, board_height


def main():
    board_width, board_height = check_board_dimensions()
    puzzle_board = PuzzleBoard(board_width, board_height)
    first_move = True
    while True:
        if first_move:
            position_row, position_column, first_move = check_input_position(board_width, board_height)
        else:
            position_row, position_column = puzzle_board.check_position()
        puzzle_board.set_position(position_row, position_column)
        puzzle_board.set_possible_moves(position_row, position_column, board_width, board_height)
        puzzle_board.finish()
        print(puzzle_board)


if __name__ == '__main__':
    main()
