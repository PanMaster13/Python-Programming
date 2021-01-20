print("Welcome to Google Grocery Store. What would you like to order?")
from decimal import Decimal
total1 = total2 = total3 = 0
ipt1 = ""
while ipt1 != "c":
    print("[V]egetable Category")
    print("[M]eat Category")
    print("[S]eafood Category")
    print("[C]alculate Order")
    print("\n")
    ipt = input("What would you like to do?")
    ipt1 = ipt.lower()

    
    if ipt1 == "s":
        print("Seafood Category")
        fish = int(input("Fish:"))
        prawn = int(input("Prawn (per 100gram):"))
        crab = int(input("Crab (per 100gram):"))
        total1 = round((fish * 1.50) + (prawn * 3.50) + (crab * 3.20),2)
        print("Subtotal for Seafood Category:", total1)

    elif ipt1 == "m":
        print("Meat section")
        chicken = int(input("Chicken (per 100gram):"))
        beef = int(input("Beef (per 100gram):"))
        lamb = int(input("Lamp (per 100gram):"))
        total2 = round((chicken * 1.20) + (beef * 3.50) * (lamb * 3.80),2)
        print("Total:", total2)

    elif ipt1 == "v":
        print("Vegetable section")
        cabbage = int(input("Cabbage:"))
        french_bean = int(input("French bean (per 100gram):"))
        broccoli = int(input("Broccoli:"))
        total3 = round((cabbage * 0.65) + (french_bean * 0.35) + (broccoli * 0.80),2)
        print("Total:", total3)

    elif ipt1 == "c":
        totalx = total1 + total2 + total3
        print("Total:", totalx)
        print("Thank you, please come again")
        
    else:
        print("Wrong input. Please try again!")

