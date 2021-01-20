def function_6():
    selection = ""
    while selection != "q":
        print("\nMathematical Calculator")
        print("\n[A]ddition")
        print("[S]ubstraction")
        print("[M]ultiplication")
        print("[D]ivision")
        print("[Q]uit")
        print("\n")
        selection = input("Selection:").lower()

        if selection == "a":
            num_1 = float(input("Enter first number:"))
            num_2 = float(input("Enter second number:"))
            ans = num_1 + num_2
            print("Addition answer:", ans)

        elif selection == "s":
            num_1 = float(input("Enter first number:"))
            num_2 = float(input("Enter second number:"))
            ans = num_1 - num_2
            print("Substraction answer:", ans)

        elif selection == "m":
            num_1 = float(input("Enter first number:"))
            num_2 = float(input("Enter second number:"))
            ans = num_1 * num_2
            print("Multiplication answer:", ans)

        elif selection == "d":
            num_1 = float(input("Enter first number:"))
            num_2 = float(input("Enter second number:"))
            ans = num_1 / num_2
            print("Division answer:", ans)

        elif selection == "q":
            print("Thank you!")

        else:
            print("Invalid selection, please try again.")


function_6()
            
        
