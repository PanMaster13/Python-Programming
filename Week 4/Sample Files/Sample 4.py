#Sample 4
#And operator
#g = "female"
#age = 18

g = input("Enter your gender:")
age = int(input("Enter your age:"))

g = g.lower() #convert input into lowercase format
 
if g ==  "female" and age <= 18:
    print("Eligible for a discount")
else:
    print("Try again next year")


