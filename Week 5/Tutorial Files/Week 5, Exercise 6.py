print("Factorial of an input number")
selection = ""
while True:
    print("Enter 'x/X' for exit.")
    ipt = input("Enter a number:")
    if ipt =="x":
        print("Thank you for using!")
        break

    elif ipt =="X":
        print("Thank you for using!")
        break

    else:
        number = int(ipt)
        fact = 1
        if number == 0:
            print("Factorial of 0 is 1")

        elif number <0:
            print("Factorial of negative numbers doesn't exist..!!")

        else:
            while number >0:
                fact=fact*number
                number=number-1
                print("The factorial of", number, "is", fact)
            

    












