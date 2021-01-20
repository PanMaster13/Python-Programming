import datetime

now = datetime.datetime.now()

print("~Today's date~")

print("Year:", now.year)

print("Month:", now.month)

print("Day:", now.day)

print("~Current time~")

print("Hour:", now.hour, "am/pm")

print("Minute:", now.minute)

print("Second:", now.second)
print("\n")


print("~New date after 5 years and 5 days later~")

print("Year:", now.year + 5)

print("Month:", now.month)

print("Day:", now.day + 5)

print("~New time: 4 hours later~")

print("Hour:", now.hour + 4, "am/pm")

print("Minute:", now.minute)

print("Second:", now.second)
print("\n")

print("~New date after 10 years and 1 month later~")

print("Year:", now.year + 10)

print("Month:", now.month + 1)

print("Day:", now.day)

print("~New time: 4 hours and 15 minutes earlier~")

print("Hour:", now.hour - 4, "am/pm")

print("Minute:", now.minute - 15)

print("Second:", now.second)
