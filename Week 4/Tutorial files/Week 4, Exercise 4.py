import calendar

print("Know more about your birthday!")
print("1. Find your birthday's day")
print("2. Find your birthday's day, n years later(based on user input)")
print("3. Find the season based on your birthday date")
print("4. Find your birthday's day, after n age (based on user input)")
ipt1 = input("Selection:")

if ipt1 == "1":
    date = input("Enter a date in YYYY/MM/DD format:").split("/")
    a = date[0]
    b = date[1]
    c = date[2]
    x = calendar.weekday(int(a), int(b), int(c))
    if x == 0:
        print("Your birthday's day is: Monday")

    elif x == 1:
        print("Your birthday's day is: Tuesday")

    elif x == 2:
        print("Your birthday's day is: Wednesday")

    elif x == 3:
        print("Your birthday's day is: Thursday")

    elif x == 4:
        print("Your birthday's day is: Friday")

    elif x == 5:
        print("Your birthday's day is: Saturday")

    elif x == 6:
        print("Your birthday's day is: Sunday")

    else:
        print("Wrong input, please try again")



elif ipt1 == "2":
    date = input("Enter a date in YYYY/MM/DD format:").split("/")
    n = int(input("n Years later:"))
    a = (int(date[0]) + n)
    b = int(date[1])
    c = int(date[2])
    x = calendar.weekday(a, b, c)
    if x == 0:
        print("In year", a, "Your birthday's day is: Monday")

    elif x == 1:
        print("In year", a, "Your birthday's day is: Tuesday")

    elif x == 2:
        print("In year", a, "Your birthday's day is: Wednesday")

    elif x == 3:
        print("In year", a, "Your birthday's day is: Thursday")

    elif x == 4:
        print("In year", a, "Your birthday's day is: Friday")

    elif x == 5:
        print("In year", a, "Your birthday's day is: Saturday")

    elif x == 6:
        print("In year", a, "Your birthday's day is: Sunday")

    else:
        print("Wrong input, please try again")


elif ipt1 == "3":
    date = input("Enter a date in YYYY/MM/DD format:").split("/")
    x = date[1]
    if x == "01" or x == "02" or x == "03":
        print("Your birth season is: Spring")

    elif x == "04" or x == "05" or x == "06":
        print("Your birth season is: Summer")

    elif x == "07" or x == "08" or x == "09":
        print("Your birth season is: Autumn")

    elif x == "10" or x == "11" or x == "12":
        print("Your birth season is: Winter")

    else:
        print("Wrong input, please try again")


elif ipt1 == "4":
    date = input("Enter a date in YYYY/MM/DD format:").split("/")
    age = int(input("Age:"))
    a = (int(date[0]) + age)
    b = int(date[1])
    c = int(date[2])
    x = calendar.weekday(a, b, c)
    if x == 0:
        print("When you are", age, "years old your birthday's day is: Monday")

    elif x == 1:
        print("When you are", age, "years old your birthday's day is: Tuesday")

    elif x == 2:
        print("When you are", age, "years old your birthday's day is: Wednesday")

    elif x == 3:
        print("When you are", age, "years old your birthday's day is: Thursday")

    elif x == 4:
        print("When you are", age, "years old your birthday's day is: Friday")

    elif x == 5:
        print("When you are", age, "years old your birthday's day is: Saturday")

    elif x == 6:
        print("When you are", age, "years old your birthday's day is: Sunday")

    else:
        print("Wrong input, please try again")


else:
    print("Wrong input, please try again")
    
              
    
    
    
    
    
    
    
    
    
    
    
    
