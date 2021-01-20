import calendar
import datetime
from datetime import timedelta
print("Month, time, day")
print("[A] To calculate new calendar based on current date & time")
print("[B] To calculate new calendar based on user input (date & time)")
ipta = input("Selection:")
print("[C] Show new calendar after n years (user input)")
print("[D] Show new date based on user input")
print("[T] Show new time based on user input")
iptb = input("Selection:")


ipt1 = ipta.lower()
ipt2 = iptb.lower()

if ipt1 == "a":
    if ipt2 == "c":
        x = datetime.date.today()
        print("Show new calendar after n years (user input)")
        year = int(input("Years:"))
        day = (year * 365)
        new_date = (x + timedelta(days=day))
        print("Date:", new_date)
        y = str(new_date).split("-")
        a = y[0]
        b = y[1]
        c = y[2]
        z = calendar.weekday(int(a), int(b), int(c))
        if z == 0:
            print("Day: Monday")

        elif z == 1:
            print("Day: Tuesday")

        elif z == 2:
            print("Day: Wednesday")

        elif z == 3:
            print("Day: Thursday")

        elif z == 4:
            print("Day: Friday")

        elif z == 5:
            print("Day: Saturday")

        elif z == 6:
            print("Day: Sunday")

        else:
            print("Wrong input, please try again")

    elif ipt2 == "d":
        x = datetime.date.today()
        print("Show new date based on user input")
        day = int(input("Days:"))
        new_date = (x + timedelta(days=day))
        print(new_date)
        y = str(new_date).split("-")
        a = y[0]
        b = y[1]
        c = y[2]
        z = calendar.weekday(int(a), int(b), int(c))
        if z == 0:
            print("Day: Monday")

        elif z == 1:
            print("Day: Tuesday")

        elif z == 2:
            print("Day: Wednesday")

        elif z == 3:
            print("Day: Thursday")

        elif z == 4:
            print("Day: Friday")

        elif z == 5:
            print("Day: Saturday")

        elif z == 6:
            print("Day: Sunday")

        else:
            print("Wrong input, please try again")

    elif ipt2 == "t":
        x = datetime.datetime.now().time().replace(microsecond=0)
        print("Show new time based on user input")
        hour = int(input("Hours:"))
        minute = int(input("Minutes:"))
        second = int(input("Seconds:"))
        time = (second + (minute * 60) + (hour * 60 * 60))
        new_time = (x + timedelta(seconds=time))
        print("Current time is:", x)
        print("New time is:", new_time)

    else:
        print("Wrong input, please try again")
        

elif ipt1 == "b":
    if ipt2 == "c":
        print("Show new calendar after n years (user input)")
        list1 = input("Enter a date in YYYY/MM/DD format:").split("/")
        year = int(input("Years:"))
        a = int(list1[0])
        b = int(list1[1])
        c = int(list1[2])
        date = datetime.datetime(a, b, c)
        day = (year * 365)
        new_date = (date+ timedelta(days=day))
        print("Date:", new_date)
        y = new_date[0]
        m = new_date[1]
        d = new_date[2]
        z = calendar.weekday(int(y), int(m), int(d))
        if z == 0:
            print("Day: Monday")

        elif z == 1:
            print("Day: Tuesday")

        elif z == 2:
            print("Day: Wednesday")

        elif z == 3:
            print("Day: Thursday")

        elif z == 4:
            print("Day: Friday")

        elif z == 5:
            print("Day: Saturday")

        elif z == 6:
            print("Day: Sunday")

        else:
            print("Wrong input, please try again")

    elif ipt2 == "d":
        print("Show new date based on user input")
        list1 = input("Enter a date in YYYY/MM/DD format:").split("/")
        day = int(input("Days:"))
        a = int(list1[0])
        b = int(list1[1])
        c = int(list1[2])
        date = datetime.datetime(a, b, c)
        new_date = (date+ timedelta(days=day))
        print("Date:", new_date)
        y = new_date[0]
        m = new_date[1]
        d = new_date[2]
        z = calendar.weekday(int(y), int(m), int(d))
        if z == 0:
            print("Day: Monday")

        elif z == 1:
            print("Day: Tuesday")

        elif z == 2:
            print("Day: Wednesday")

        elif z == 3:
            print("Day: Thursday")

        elif z == 4:
            print("Day: Friday")

        elif z == 5:
            print("Day: Saturday")

        elif z == 6:
            print("Day: Sunday")

        else:
            print("Wrong input, please try again")

    elif ipt2 == "t":
        print("Show new time based on user input:")
        old_time = input("Enter a time in hh:mm:ss format:")
        hour = int(input("Hours:"))
        minute = int(input("Minutes:"))
        second = int(input("Seconds:"))
        time = (second + (minute * 60) + (hour * 60 * 60))
        new_time = (x + timedelta(seconds=time))
        print("Current time is:", x)
        print("New time is:", new_time)

    else:
        print("Wrong input, please try again")

else:
        print("Wrong input, please try again")

        
        
        






        
