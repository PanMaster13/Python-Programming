selection = "".lower


int_value = end_value = count_value = 0

while selection != "x":
    print("While Loop program")
    int_value = int(input("Enter Initial value:"))
    end_value = int(input("Enter Ending value:"))
    print("To increase/decrease the loop")
    count_value = int(input("Enter Counter value:"))
    if count_value <0:
        print("Decrease loop")
        while int_value > end_value:
            print(int_value)
            int_value -=count_value
    
    elif count_value >0:
        print("Increase loop")
        while int_value < end_value:
            print(int_value)
            int_value -=count_value

    selection = input("Enter c to continue and x to exit:")

            
