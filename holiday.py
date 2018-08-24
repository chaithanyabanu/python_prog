from datetime import date
from datetime import datetime
def holiday(day):
	if day%6==0 or day%5==0:
		print("hii this is weekend you can enjoy holiday")

	else:
		print("come to the office immediately")

date_to_check_holiday=input("enter the date required to check")

day=int(input("enter the day"))
month=int(input("enter the month"))
year=int(input("enter the year"))
today=date(year,month,day)
day_count=today.weekday()
print(day_count)
holiday(day_count)
