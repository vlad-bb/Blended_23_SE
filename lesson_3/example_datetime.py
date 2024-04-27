import time


from datetime import datetime
import calendar


date = '2022/04/20 09:00'
print(type(date))
date_object = datetime.strptime(date, "%Y/%m/%d %H:%M")
print(type(date_object))
date_string = datetime.strftime(date_object, '%d %m %Y %H:%M')
print(date_string)

current_date = datetime.now()
print(current_date, type(current_date))

currecnt_day = datetime.today().date()
print(currecnt_day, type(currecnt_day))

delta_ = (currecnt_day - date_object.date()).days
print(delta_)
print(calendar.isleap(2024))