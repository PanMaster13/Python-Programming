#Repeat the selection until select "Quit"


selection = ""
num1 = num2 = 0

while selection != "3":
    print("""
[1] Addition
[2] Subtraction
[3] Quit
""")
    selection = input("Your selection:")
    if selection == "1":
        num1 = float(input("First number:"))
        num2 = float(input("Second number:"))

        ans = num1 + num2
        print("Answer:", ans, "\n")

    elif selection == "2":
        num1 = float(input("First number:"))
        num2 = float(input("Second number:"))

        ans = num1 - num2
        print("Answer:", ans, "\n")

    elif selection == "3":
        print("Thank you. Please come again\n")
    else:
        print("Wrong input, try again!")

    
