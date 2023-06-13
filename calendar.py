import datetime
import re


def note(user_answer):
    counter = 1
    while user_answer > 0:
        date = input(f"Enter date and time of note #{counter} (in format «YYYY-MM-DD HH:MM»):\n")
        while not re.match(r'\d{4}-\d\d-\d\d\s\d\d:\d\d', date):
            date = input("Incorrect format. Please try again (use the format «YYYY-MM-DD HH:MM»):\n")
        while not re.match('(0[1-9]|1[0-2])', re.split('[-\\s:]', date)[1]):
            date = input("Incorrect month value. The month should be in 1-12.\nPlease try again:\n")
        while not re.match('(0[1-9]|[12][0-9]|3[01])', re.split('[-\\s:]', date)[2]):
            date = input("Incorrect day value. The day should be in 1-31.\nPlease try again:\n")
        while not re.match('([01][0-9]|2[0-3])', re.split('[-\\s:]', date)[3]):
            date = input("Incorrect hour value. The hour should be in 00-23.\nPlease try again:\n")
        while not re.match('([0-5][0-9])', re.split('[-\\s:]', date)[4]):
            date = input("Incorrect minute value. The minutes should be in 00-59.\nPlease try again:\n")
        check_date = re.split('[-\\s:]', date)
        text = input(f"Enter text of note #{counter}:\n")
        with open("notes.txt", "a") as file:
            file.write(f"{check_date[2]}/{check_date[1]}/{check_date[0]} {check_date[3]}:{check_date[4]} >{text}\n")
        counter += 1
        user_answer -= 1
    print("Notes added!")


def poll():
    user_answer = input("Let's change several notes in the calendar.\nHow many notes do you want to add or delete? "
                        "(enter a positive number to add or a negative to remove)\n")
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("You can only enter numbers consisting of digits, not text! Enter a positive number to add or a negative "
              "to remove")
        poll()
    return int(user_answer)


def del_note(user_answer):
    with open("notes.txt", "r") as file:
        lines = file.readlines()
    counter = 0
    while user_answer < 0:
        pick_note = input(["Enter the text of the note you want to delete:\n", "No notes with such text were found. "
                                                                               "Try again:\n"][bool(counter)])
        for line in lines:
            if f"{pick_note}\n" not in line:
                counter += 1
                continue
            else:
                with open("notes.txt", "w") as file:
                    for line in lines:
                        if f"{pick_note}\n" not in line:
                            file.write(line)
                user_answer += 1
                counter = 0
                print("Note deleted!")


def read_note():
    with open("notes.txt", "r") as file:
        for line in file:
            event = datetime.datetime.strptime(line[:line.find(">") - 1], "%d/%m/%Y %H:%M")
            time_delta = event - datetime.datetime.now()
            delta_days = time_delta.days
            delta_hours = time_delta.seconds // 3600
            delta_minutes = (time_delta.seconds - delta_hours * 3600) // 60
            text = line[line.find(">") + 1: - 1]
            print(f'Before the event note "{text}" remains:\n{delta_days} day(s), {delta_hours} hour(s) '
                  f'{delta_minutes} minute(s)')


def main():
    print(f"Current date and time: \n{datetime.datetime.now()}")
    read_note()
    user_answer = poll()
    if user_answer > 0:
        note(user_answer)
    elif user_answer < 0:
        del_note(user_answer)
    elif user_answer == 0:
        pass
    read_note()


if __name__ == '__main__':
    main()
