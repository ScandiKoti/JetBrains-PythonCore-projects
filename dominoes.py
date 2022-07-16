import random
from collections import Counter


def list_dominos():
    list_of_dominos = [[i, j] for i in range(7) for j in range(i, 7)]
    return list_of_dominos


def print_table(status):
    print('=' * 70, f'\nStock size: {len(stock_pieces)}\nComputer pieces: {len(comp_pieces)}\n')
    if len(domino_board) < 7:
        for lst in domino_board:
            print(lst, end='')
        print(f'\n\nYour pieces:')
    else:
        print(
            f'{domino_board[0]}{domino_board[1]}{domino_board[2]}...{domino_board[-3]}{domino_board[-2]}\
{domino_board[-1]}')
        print(f'\nYour pieces:')
    for piece in player_pieces:
        print(f"""{(1 + player_pieces.index(piece))}:{piece}""")
    check_win(status)


def check_win(status):
    if len(player_pieces) == 0:
        print('The game is over. You won!')
        exit()
    elif len(comp_pieces) == 0:
        print('The game is over. The computer won!')
        exit()
    elif domino_board[0][0] == domino_board[-1][-1] and domino_board.count(domino_board[0][0]) == 8 or \
            len(stock_pieces) == 0 and len([i for i in comp_pieces if i[1] == domino_board[0][0] or \
                                                                      i[1] == domino_board[-1][-1] or \
                                                                      i[0] == domino_board[0][0] or \
                                                                      i[0] == domino_board[-1][-1]]) == 0 and \
            len([i for i in player_pieces if i[1] == domino_board[0][0] or i[1] == domino_board[-1][-1] or \
                                             i[0] == domino_board[0][0] or i[0] == domino_board[-1][-1]]) == 0:
        print("Status: The game is over. It's a draw!")
        exit()
    else:
        print(f'\nStatus: {status}')
        game(status)


def is_digit(inp):
    if inp[0] in ('-', '+'):
        return inp[1:].isdigit()
    return inp.isdigit()


def game(status):
    index = input()
    if status == "It's your turn to make a move. Enter your command.":
        if is_digit(index) is False or abs(int(index)) > len(player_pieces):
            print('Invalid input. Please try again.')
            game(status)
        else:
            index = int(index)
            if index == 0:
                if len(stock_pieces) > 0:
                    index = random.randint(0, (len(stock_pieces) - 1))
                    piece = stock_pieces[index]
                    player_pieces.append(piece)
                    stock_pieces.pop(stock_pieces.index(piece))
                else:
                    status = "Computer is about to make a move. Press Enter to continue..."
                    print_table(status)
            elif index > 0 and domino_board[-1][-1] in player_pieces[index - 1]:
                if player_pieces[index - 1][0] == domino_board[-1][-1]:
                    piece = player_pieces[index - 1]
                    domino_board.append(piece)
                else:
                    piece = player_pieces[index - 1]
                    domino_board.append(piece[::-1])
                player_pieces.pop(player_pieces.index(piece))
            elif index < 0 and domino_board[0][0] in player_pieces[abs(index) - 1]:
                if player_pieces[abs(index) - 1][-1] == domino_board[0][0]:
                    piece = player_pieces[abs(index) - 1]
                    domino_board.insert(0, piece)
                else:
                    piece = player_pieces[abs(index) - 1]
                    domino_board.insert(0, piece[::-1])
                player_pieces.pop(player_pieces.index(piece))
            else:
                print("Illegal move. Please try again.")
                game(status)
        status = "Computer is about to make a move. Press Enter to continue..."
        print_table(status)
    elif status == "Computer is about to make a move. Press Enter to continue...":
        comp_turn = [i for i in comp_pieces if i[1] == domino_board[0][0] or i[1] == domino_board[-1][-1] or \
                     i[0] == domino_board[0][0] or i[0] == domino_board[-1][-1]]
        temp_list = comp_turn + domino_board
        check_list = sum(temp_list, [])
        freq_counter = Counter(check_list)
        scores = [freq_counter[comp_turn[i][0]] + freq_counter[comp_turn[i][1]] for i in range(len(comp_turn))]
        if len(comp_turn) > 0:
            scores_max = max(scores)
            scores_max_index = scores.index(scores_max)
            piece = comp_turn[scores_max_index]
            if comp_turn[scores_max_index][0] == domino_board[-1][-1]:
                domino_board.append(piece)
            elif comp_turn[scores_max_index][1] == domino_board[-1][-1]:
                domino_board.append(piece[::-1])
            elif comp_turn[scores_max_index][-1] == domino_board[0][0]:
                domino_board.insert(0, piece)
            elif comp_turn[scores_max_index][-2] == domino_board[0][0]:
                domino_board.insert(0, piece[::-1])
            comp_pieces.pop(comp_turn.index(piece))
        else:
            if len(stock_pieces) > 0:
                index = random.randint(0, len(stock_pieces))
                piece = stock_pieces[index - 1]
                comp_pieces.append(piece)
                stock_pieces.pop(stock_pieces.index(piece))
            else:
                status = "It's your turn to make a move. Enter your command."
                print_table(status)
        status = "It's your turn to make a move. Enter your command."
        print_table(status)


while True:
    list_of_dominos = list_dominos()
    random.shuffle(list_of_dominos)
    player_pieces = list_of_dominos[:7]
    comp_pieces = list_of_dominos[21:]
    stock_pieces = list_of_dominos[7:21]
    domino_board = []
    double_dominos = [j for j in player_pieces + comp_pieces if j[0] == j[1]]
    if len(double_dominos) == 0:
        continue
    max_piece = max(double_dominos)
    if max_piece in player_pieces:
        player_pieces.pop(player_pieces.index(max_piece))
        status = "Computer is about to make a move. Press Enter to continue..."
    else:
        comp_pieces.pop(comp_pieces.index(max_piece))
        status = "It's your turn to make a move. Enter your command."
    domino_board.append(max_piece)
    print_table(status)
    game(status)
    break
