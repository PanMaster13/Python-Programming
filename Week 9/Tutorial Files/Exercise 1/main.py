import menu
import add
import calculate

choice = " "
while choice != "2":
    choice = menu.main_menu()

    if choice == "1":
        add.adding()

    elif choice == "2":
        break

    else:
        print("Invalid input, please try again.")

calculate.calculate()
 
