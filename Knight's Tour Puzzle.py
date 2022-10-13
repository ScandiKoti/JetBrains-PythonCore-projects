class PuzzleBoard:
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.cell_size = len(str(self.column * self.row))
        self.grid = [['_' * self.cell_size for _ in range(self.column)] for _ in range(self.row)]
        self.possible_moves = [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]]
        self.temp_possible_moves = []
        self.position = 2

    def __str__(self):
        board = " " + "-" * (self.column * (self.cell_size + 1) + 3) + "\n"
        for i in range(self.row, 0, -1):
            board += f'{i}| {" ".join(self.grid[i - 1])} |\n'
        board += " " + "-" * (self.column * (self.cell_size + 1) + 3) + "\n"
        board += ' ' * 3 + " ".join((" " * (self.cell_size - len(str(x))) + str(x + 1)) for x in range(self.column)) \
                 + '\n'
        return board

    def solve_board(self, position_row, position_column):
        if self.position == self.row * self.column + 1:
            return True
        for move in self.possible_moves:
            move_column, move_row = move
            if 0 <= position_row + move_row < self.row and 0 <= position_column + move_column < self.column and \
                    self.grid[position_row + move_row][position_column + move_column] == '_' * self.cell_size:
                self.grid[position_row + move_row][position_column + move_column] =\
                    ' ' * (self.cell_size - len(str(self.position))) + str(self.position)
                self.position += 1
                if self.solve_board(position_row + move_row, position_column + move_column):
                    return True
                self.position -= 1
                self.grid[position_row + move_row][position_column + move_column] = '_' * self.cell_size
        return False

    def set_position(self, position_row, position_column):
        for i in range(self.row):
            for j in range(self.column):
                if self.check_visited(i, j):
                    self.grid[i][j] = ' ' * (self.cell_size - 1) + '*'
                else:
                    self.grid[i][j] = '_' * self.cell_size
        self.grid[position_row][position_column] = ' ' * (self.cell_size - 1) + 'X'

    def set_possible_moves(self, position_row, position_column):
        for move in self.possible_moves:
            move_row, move_column = move
            if 0 <= (position_column + move_column) < self.column and 0 <= (position_row + move_row) < self.row and \
                    not self.check_visited((position_row + move_row), (position_column + move_column)):
                move_column, move_row = (position_column + move_column), (position_row + move_row)
                self.temp_possible_moves.append([move_column + 1, move_row + 1])
                counter = PuzzleBoard.possible_moves_counter(self, move_row, move_column)
                self.grid[move_row][move_column] = ' ' * (self.cell_size - 1) + str(counter)

    def check_visited(self, position_row, position_column):
        if self.grid[position_row][position_column] in \
                [' ' * (self.cell_size - 1) + 'X', ' ' * (self.cell_size - 1) + '*']:
            return True
        return False

    def possible_moves_counter(self, move_row, move_column):
        counter = -1
        for next_move in self.possible_moves:
            next_move_row, next_move_column = next_move
            if 0 <= (move_column + next_move_column) < self.column and 0 <= (
                    move_row + next_move_row) < self.row:
                counter += 1
        return counter

    def check_position(self):
        while True:
            state = input("Enter your next move: ").split()
            try:
                state = [int(i) for i in state]
                position_row = state[1] - 1
                position_column = state[0] - 1
                if len(state) != 2:
                    raise ValueError
                elif list(state) not in self.temp_possible_moves:
                    raise IndexError
            except (ValueError, IndexError):
                print("Invalid move!", end=' ')
                continue
            break
        self.temp_possible_moves = []
        return position_row, position_column

    def check_input_position(self):
        while True:
            state = input("Enter the knight's starting position: ").split()
            try:
                position_row = int(state[1]) - 1
                position_column = int(state[0]) - 1
                first_move = False
                if len(state) != 2:
                    raise ValueError
                elif not (0 <= position_column < self.column and 0 <= position_row < self.row):
                    raise IndexError
            except (ValueError, IndexError):
                print("Invalid position!")
                continue
            break
        return position_row, position_column, first_move

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


def check_board_dimensions():
    while True:
        board_dimensions = input("Enter your board dimensions:").split()
        try:
            board_width = int(board_dimensions[0])
            board_height = int(board_dimensions[1])
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
            position_row, position_column, first_move = puzzle_board.check_input_position()
            puzzle_board.grid[position_row][position_column] = ' ' * (puzzle_board.cell_size - 1) + "1"
            while True:
                solution = input("Do you want to try the puzzle? (y/n):")
                solve_board = puzzle_board.solve_board(position_row, position_column)
                if solution == "n":
                    if not solve_board:
                        print("No solution exists!")
                    else:
                        print("Here's the solution!")
                        print(puzzle_board)
                    exit()
                elif solution == "y":
                    if not solve_board:
                        print("No solution exists!")
                        exit()
                    else:
                        puzzle_board.grid = [['_' * puzzle_board.cell_size for _ in range(board_width)] for _ in
                                             range(board_height)]
                        break
                else:
                    print("Invalid input!")
                    continue
        else:
            position_row, position_column = puzzle_board.check_position()
        puzzle_board.set_position(position_row, position_column)
        puzzle_board.set_possible_moves(position_row, position_column)
        puzzle_board.finish()
        print(puzzle_board)


if __name__ == '__main__':
    main()
