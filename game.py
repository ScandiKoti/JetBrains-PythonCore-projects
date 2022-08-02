import random


def check(rating, lst_options):
    while True:
        check_options = lst_options + ["!exit", "!rating"]
        check_input = input()
        if check_input in check_options:
            if check_input == "!exit":
                print("Bye!")
                exit()
            elif check_input == "!rating":
                print(f"Your rating: {rating}")
                continue
            return check_input
        print("Invalid input")


def game():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    options = input()
    print("Okay, let's start")
    user_rating = 0
    rating_file = open('rating.txt', 'r')
    for line in rating_file:
        line_lst = line.split()
        if line_lst[0] == user_name:
            user_rating = int(line_lst[1])
    rating_file.close()
    while True:
        if options == "":
            options = "rock,paper,scissors"
        list_options = options.split(",")
        user_input = check(user_rating, list_options)
        index_user_input = list_options.index(user_input)
        temp_list = list_options[index_user_input + 1:] + list_options[:index_user_input]
        len_slice = int(len(temp_list) / 2)
        win_options = temp_list[:len_slice]
        loss_options = temp_list[len_slice:]
        comp_move = random.choice(list_options)
        if user_input == comp_move:
            user_rating += 50
            print(f"There is a draw {comp_move}")
        elif comp_move in win_options:
            print(f"Sorry, but the computer chose {comp_move}")
        elif comp_move in loss_options:
            user_rating += 100
            print(f"Well done. The computer chose {comp_move} and failed")


game()
