x = int(input("Input birthday:"))
y = input("Input month of birth (e.g. March, July etc):")

if (y == "January" and (x >= 20 and x <= 31)) or (y == "February" and (x >= 1 and x <= 18)):
    print("Your Astrological sign is : Aquarius")

elif (y == "February" and (x >= 19 and x <= 29)) or (y == "March" and (x >= 1 and x <= 20)):
    print("Your Astrological sign is : Pices")

elif (y == "March" and (x >= 21 and x <= 31)) or (y == "April" and (x >= 1 and x <= 19)):
    print("Your Astrological sign is : Aries")

elif (y == "April" and (x >= 20 and x <= 30)) or (y == "May" and (x >= 1 and x <= 20)):
    print("Your Astrological sign is : Taurus")

elif (y == "May" and (x >= 21 and x <= 31)) or (y == "June" and (x >= 1 and x <= 20)):
    print("Your Astrological sign is : Gemini")

elif (y == "June" and (x >= 21 and x <= 30)) or (y == "July" and (x >= 1 and x <= 22)):
    print("Your Astrological sign is : Cancer")

elif (y == "July" and (x >= 23 and x <= 31)) or (y == "August" and (x >= 1 and x <= 22)):
    print("Your Astrological sign is : Leo")

elif (y == "August" and (x >= 23 and x <= 31)) or (y == "September" and (x >= 1 and x <= 22)):
    print("Your Astrological sign is : Vigro")

elif (y == "September" and (x >= 23 and x <= 30)) or (y == "October" and (x >= 1 and x <= 22)):
    print("Your Astrological sign is : Libra")

elif (y == "October" and (x >= 23 and x <= 31)) or (y == "November" and (x >= 1 and x <= 21)):
    print("Your Astrological sign is : Scorpio")

elif (y == "November" and (x >= 22 and x <= 30)) or (y == "Decenber" and (x >= 1 and x <= 21)):
    print("Your Astrological sign is : Sagittarius")

elif (y == "December" and (x >= 22 and x <= 31)) or (y == "January" and (x >= 1 and x <= 19)):
    print("Your Astrological sign is : Capricorn")

else:
    print("Incorrect day or name of month")
