import random


def check_dif_level():
    while True:
        user_dif_level = int(input('Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n'
                                   '2 - integral squares of 11-29\n'))
        level_list = [1, 2]
        if user_dif_level in level_list:
            return user_dif_level
        else:
            print("Incorrect format.")


def check_input():
    while True:
        try:
            user_answer = int(input())
            return user_answer
        except ValueError:
            print('Incorrect format.')


def task_gen(level):
    if level == 1:
        a = str(random.randint(2, 9))
        b = str(random.randint(2, 9))
        operator = random.choice(['+', '-', '*'])
        task = a + operator + b
        print(task)
        return eval(task)
    elif level == 2:
        a = random.randint(11, 29)
        task = a
        print(task)
        return a ** 2


def validate_answer():
    counter, mark = 0, 0
    user_dif_level = check_dif_level()
    while counter < 5:
        eval_task = task_gen(user_dif_level)
        user_answer = check_input()
        if user_answer == eval_task:
            mark += 1
            print('Right!')
        else:
            print('Wrong!')
        counter += 1
    print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
    level_description = {1: "(simple operations with numbers 2-9)", 2: "(integral squares of 11-29)"}
    save_input = input()
    if save_input in ('yes', 'YES', 'y', 'Yes'):
        print('What is your name?')
        user_name = input()
        with open('results.txt', 'a') as file:
            file.write(f'{user_name}: {mark}/5 in level {user_dif_level} {level_description[user_dif_level]}')
        print('The results are saved in "results.txt".')
    else:
        exit()


validate_answer()
