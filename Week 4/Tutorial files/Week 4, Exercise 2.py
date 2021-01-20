print("Google Grocery shop")
print("[V]egetable selection")
print("[M]eat selection")
print("[S]eafood selection")
print("\n")
ipt = input("Enter your selection:")
ipt1 = ipt.lower()

if ipt1 == "s":
    print("Seafood section")
    fish = int(input("Fish:"))
    prawn = int(input("Prawn (per 100gram):"))
    crab = int(input("Crab (per 100gram):"))
    total = (fish * 6.50) + (prawn * 6.80) + (crab * 5.90)
    print("Total:", total)

elif ipt1 == "m":
    print("Meat section")
    chicken = int(input("Chicken (per 100gram):"))
    beef = int(input("Beef (per 100gram):"))
    lamb = int(input("Lamb (per 100gram):"))
    total = (chicken * 8.50) + (beef * 12.50) * (lamb * 13.50)
    print("Total:", total)

elif ipt1 == "v":
    print("Vegetable section")
    cabbage = int(input("Cabbage:"))
    french_bead = int(input("French bead (per 100gram):"))
    brinjal = int(input("Brinjal (per 100gram):"))
    broccoli = int(input("Broccoli:"))
    total = (cabbage * 2.30) + (french_bead *1.50) + (brinjal * 1.20) + (broccoli * 1.80)
    print("Total:", total)

else:
    print("Wrong input. Please try again!")
    
print("\n")
      
paid = float(input("Amount Paid:"))
change = (paid - total)
from decimal import Decimal
opt = round(change,2)
print("Change:", opt)

optx100 = (opt * 100)
optprcnt = int(optx100)

dollar = int(optprcnt / 100)
print("Dollar            :", dollar)

quarter = (optprcnt % 100) / 25
print("Quarter (25 cents):", int(quarter))

dime = ((optprcnt % 100) % 25) /10
print("Dime (10 cents)   :", int(dime))

nickle = (((optprcnt % 100) % 25) % 10) / 5
print("Dime (5 cents)    :", int(nickle))

penny = ((((optprcnt % 100) % 25) % 10) % 5) / 1
print("Penny (1 cent)    :", int(penny))













    
               

