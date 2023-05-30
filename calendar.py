import datetime


print(f"Current date and time: \n{datetime.datetime.now()}\nLet's add a note to the calendar.")
year = input("Enter year:\n")
month = input("Enter month:\n")
day = input("Enter day:\n")
hour = input("Enter hour:\n")
minute = input("Enter minute:\n")
text = input("Enter a text:\n")
event = datetime.datetime.strptime(f"{day}/{month}/{year} {hour}:{minute}", "%d/%m/%Y %H:%M")
time_delta = event - datetime.datetime.now()
delta_days = time_delta.days
delta_hours = time_delta.seconds // 3600
delta_minutes = (time_delta.seconds - delta_hours * 3600) // 60
print(f'Before the event note "{text}" remains:\n{delta_days} day(s), {delta_hours} hour(s) {delta_minutes} minute(s)')
