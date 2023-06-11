import datetime
import re


def note():
    date = input("Let's add a note to the calendar.\nEnter date and time (in format «YYYY-MM-DD HH:MM»):\n")
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
    text = input("Enter a text:\n")
    with open("notes.txt", "a") as file:
        file.write(f"{check_date[2]}/{check_date[1]}/{check_date[0]} {check_date[3]}:{check_date[4]} >{text}\n")


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
