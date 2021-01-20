#user input date
#sample 6

import datetime

date_entry = input("Enter a date yyyy-mm-dd:")
year, month, day = map(int, date_entry.split("-"))

input_year =  int(input("Enter years:"))

mydate = datetime.date(year+input_year, month, day)

print(mydate)
