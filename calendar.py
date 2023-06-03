import datetime


def note():
    year = input("Let's add a note to the calendar.\nEnter year:\n")
    month = input("Enter month:\n")
    day = input("Enter day:\n")
    hour = input("Enter hour:\n")
    minute = input("Enter minute:\n")
    text = input("Enter a text:\n")
    with open("notes.txt", "a") as file:
        file.write(f"{day}/{month}/{year} {hour}:{minute} >{text}\n")


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
    note()
    read_note()


if __name__ == '__main__':
    main()
