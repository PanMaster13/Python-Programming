print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
x = input("Input the name of Month:")

list1 = ["February"]
list2 = ["January", "March", "May", "July", "August", "October", "December"]
list3 = ["April", "June", "September", "November"]

if x in list1:
    print("No. of days: 28/29 days")

elif x in list2:
    print("No. of days: 31 days")

elif x in list3:
    print("No. of days: 30 days")

else:
    print("Incorrect name of month")
    

