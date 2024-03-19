"""
Задача
Є заннятя з йоги на 9:00 по UTC lesson = “17-03-2024 09:00”
кліент живе в Киеві
тренер живе в Індії(Делі)
Написати функцію яка відобраражає місцевий час для користувача
def show_local_time(lesson: str, role: str) -> str:
    pass
спробуйте різними шляхами написати рішення
Перевірити можно тут https://time.is/uk/compare/0900_19_Mar_2024_in_UTC/Kyivets/National_Capital_Territory_of_Delhi
"""

# Solution from Mykhailo
from datetime import datetime, timedelta


def show_local_time(lesson: str, role: str) -> str:
    lesson_UTC = datetime.strptime(lesson, "%d-%m-%Y %H:%M")
    if role.lower() == "client":
        lesson_lokal = lesson_UTC + timedelta(hours=+2)
    elif role.lower() == "coach":
        lesson_lokal = lesson_UTC + timedelta(hours=+5, minutes=30)
    else:
        print("Input your status as client or coach")
    return lesson_lokal.strftime("%d-%m-%Y %H:%M")


print("# Solution from Mykhailo")
lesson = "17-03-2024 09:00"
role = input("Please input your status (client or coach) >>> ")
local_time = show_local_time(lesson, role)
print(f"Local time for {role}: {local_time}")

# Solution from Rehina
from datetime import datetime
import pytz


def show_local_time(lesson: str, role: str) -> str:
    deli_timezone = pytz.timezone('Asia/Kolkata')
    kyiv_timezone = pytz.timezone('Europe/Kiev')
    lesson1 = datetime.strptime(lesson, "%d-%m-%Y %H:%M")
    current_time1 = deli_timezone.localize(lesson1).astimezone(kyiv_timezone)
    if role == 'Kyiv':
        return current_time1
    else:
        return lesson1


print("# Solution from Rehina")
print(show_local_time("17-03-2024 09:00", "Kyiv"))
print(show_local_time("17-03-2024 09:00", "Deli"))

# Solution from mentor

from datetime import datetime
from pytz import timezone, utc


def show_local_time(lesson: str, role: str) -> str:
    """Функція показує місцевий час для користувача"""
    lesson_dt_obj = utc.localize(datetime.strptime(lesson, "%d-%m-%Y %H:%M"))
    if role.lower() == "client":
        local_dt_obj = lesson_dt_obj.astimezone(timezone('Europe/Kiev'))
    elif role.lower() == "coach":
        local_dt_obj = lesson_dt_obj.astimezone(timezone('Asia/Kolkata'))
    else:
        return "Input your status as client or coach"
    return local_dt_obj.strftime("%d-%m-%Y %H:%M")


print("# Solution from mentor")
lesson = "17-03-2024 09:00"
roles = ["client", "coach"]
for role in roles:
    local_time = show_local_time(lesson, role)
    print(f"Local time for {role}: {local_time}")
