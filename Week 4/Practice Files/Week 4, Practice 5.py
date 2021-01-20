x = input("Input the month (e.g. January, February etc.):")
y = int(input("Input the day:"))
list1 = ["March", "April", "May"]
list2 = ["June", "July", "August"]
list3 = ["September", "October", "November"]
list4 = ["December", "January", "February"]

if x in list1 and y >= 1 and y <= 31:
    print("Season is spring")

elif x in list2 and y >= 1 and y <= 31:
    print("Season is summer")

elif x in list3 and y >= 1 and y <= 31:
    print("Season is autumn")

elif x in list4 and y >= 1 and y <= 31:
    print("Season is winter")

else:
    print("Incorrect name of month or day")
    
