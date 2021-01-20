def file():
    selection = input("Do you want to keep a record (y/n):").lower()
    if selection == "y":
        output = "Yes"

    elif selection == "n":
        print("Thank you. Please come again.")
        output = "No"

    else:
        print("Wrong input. Please try again.")
        output = "Wrong"

    return output

