import random


num_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if num_of_friends < 1:
    print("No one is joining for the party")
    exit()
friends_dict = {}
print("Enter the name of every friend (including you), each on a new line:")
friends_dict.update({input(): 0 for _ in range(num_of_friends)})
total_bill = int(input("Enter the total bill value:\n"))
split_value = round(total_bill / num_of_friends, 2)
lucky_split_value = round(total_bill / (num_of_friends - 1), 2)
check_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if check_lucky != "Yes":
    print("No one is going to be lucky\n")
    friends_dict.update({key: split_value for key in friends_dict})
    print(friends_dict)
    exit()
lucky = random.choice(list(friends_dict.keys()))
print(f"{lucky} is the lucky one!\n")
friends_dict.update({key: lucky_split_value for key in friends_dict})
friends_dict[lucky] = 0
print(friends_dict)
