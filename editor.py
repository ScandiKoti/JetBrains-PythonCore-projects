def plain():
    return f'{input("Text: ")}'


def bold():
    return f'**{input("Text: ")}**'


def italic():
    return f'*{input("Text: ")}*'


def header():
    while True:
        level = int(input("Level: "))
        if 0 < level < 7:
            return "#"*level + " " + input("Text: ") + "\n"
        else:
            print("The level should be within the range of 1 to 6")


def link():
    label = input("Label: ")
    return f'[{label}]({input("URL: ")})'


def inline_code():
    return f'`{input("Text: ")}`'


def new_line():
    return "\n"


def lst(choice):
    while True:
        rows = int(input("Number of rows:"))
        if rows > 0:
            text = ''
            for i in range(1, rows + 1):
                row = input(f"Row #{i}:")
                if choice == "unordered-list":
                    text += "* " + row + "\n"
                else:
                    text += f"{i}. " + row + "\n"
            return text
        else:
            print("The number of rows should be greater than zero")


formatters = {"plain": plain, "bold": bold, "italic": italic, "header": header, "link": link,
              "inline-code": inline_code, "new-line": new_line, "ordered-list": lambda: lst(user_choice),
              "unordered-list": lambda: lst(user_choice)}
commands = ['!help', '!done']
user_help = 'Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list\n' \
            'Special commands: !help !done'
user_text = str()
while True:
    user_choice = input('Choose a formatter:')
    if user_choice in formatters:
        user_text += formatters[user_choice]()
        print(user_text)
    elif user_choice in commands:
        if user_choice == '!help':
            print(user_help)
        elif user_choice == '!done':
            with open('output.md', 'w') as file:
                file.write(user_text)
            exit()
    else:
        print('Unknown formatting type or command')
