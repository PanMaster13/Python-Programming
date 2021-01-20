import gardenFunction #importing module
import textGUI #importing module

input_1 = "incorrect" #initial state of the first input
input_2 = "incorrect" #initial state of the second input
input_3 = "incorrect" #initial state of the third input

while (input_1 == "incorrect") or (input_2 == "incorrect") or (input_3 == "incorrect"): 
    name = input("Customer Name:") #first input
    number = input("Contact Number:") #second input
    people = input("No. of People:") #third input
   
    validation_1 = gardenFunction.validateCustomerName(name) #validating name using function in module

    if validation_1 == False: #failed validation
        print("Invalid Name") #error message
        input_1 = "incorrect" #resetting state of input in case it changed

    else:
        input_1 = "correct" #breaking while loop as it passed validation
    
    
    validation_2 = gardenFunction.validatePhoneNumber(number) #validating phone number using function in module

    if validation_2 == True: #passed validation
        input_2 = "correct" #breaking while loop
        
    else:
        print("Invalid Phone Number") #error message as it failed validation
        input_2 = "incorrect" #resetting state of input in case it changed
    
    
    
    validation_3 = gardenFunction.validateNoOfPeople(people) #validating number of people using function in module

    if validation_3 == -1: #failed validation
        print("Invalid No. of People") #error message
        input_3 = "incorrect" #resetting state of input in case it changed

    else:
        input_3 = "correct" #breaking while loop as it passed validation


textGUI.printBanner() #printing banner using function in module

textGUI.printVenue() #printing venue option using function in module
venueList = gardenFunction.readVenueList("venue.txt") #creating venue list using function in module

input_4 = "incorrect" #initial state of the fourth input
while input_4 =="incorrect":
    venue_choice = input("Please select a Venue:") #fourth input
    validation_4 = gardenFunction.validateVenue(venue_choice, venueList, int(people)) #validating venue using function in module
    if validation_4 == True: #passed validation
        input_4 = "correct" #breaking while loop

    elif validation_4 == False: #failed validation
        print("Invalid venue, please select another venue") #error message

    else:
        print("Invalid input, please try again.") #incorrect input message



textGUI.printMenuPackage() #printing menu option using function in module

input_5 = "incorrect" #initial state of the fifth input
input_6 = "incorrect" #initial state of the sixth input
while input_6 == "incorrect":
    while input_5 == "incorrect":
        menu_selection = input("Please select a menu:") #fifth input
        if menu_selection == "1":
            textGUI.printPackage(gardenFunction.readitemList("menu/Menu1.txt")) #prints first menu
            input_5 = "correct" #breaking while loop

        elif menu_selection == "2":
            textGUI.printPackage(gardenFunction.readitemList("menu/Menu2.txt")) #prints second menu
            input_5 = "correct" #breaking while loop

        elif menu_selection == "3":
            textGUI.printPackage(gardenFunction.readitemList("menu/Menu3.txt")) #prints third menu
            input_5 = "correct" #breaking while loop
    
        elif menu_selection == "4":
            textGUI.printPackage(gardenFunction.readitemList("menu/Menu4.txt")) #prints fourth menu
            input_5 = "correct" #breaking while loop

        else:
            print("Invalid input, please try again.") #incorrect input message

    menu_decision = input("Please select choice:") #sixth input
    if menu_decision == "1": #user is satisfied with menu package
        input_6 = "correct" #breaking while loop

    elif menu_decision == "2": #user wishes to re-select menu package
        print("Please re-select your menu choice.")
        input_5 = "incorrect" #resetting fifth input to incorrect state to restart previous loop

    else:
        print("Invalid choice.") #incorrect input message

entertain_price = float(0) #initial price for entertainment (No entertainment)
entertainment = "None" #intial selection of entertainment (No entertainment
if venue_choice == "1" or venue_choice == "2": #which are VIP room and Executive room
    entertain_price = float(0) #due to the two rooms with no entertainment availability
    entertainment = "None" #due to the two rooms with no entertainment availability

else: #indicating that the venue chosen has entertainment availability
    print("""Would you like to add on entertainment?
[1] Yes
[2] No
""") 
    input_7 = "incorrect" #initial state of the seventh input
    while input_7 == "incorrect":
        entertain_choice = input("Please select choice:") #seventh input
        if entertain_choice == "1": #user wants entertainment
            textGUI.printEntertainment(venue_choice, gardenFunction.readitemList("addon/entertainment.txt")) #prints entertainment list based on respective venue
            input_8 = False #initial state of eighth input
            while input_8 == False:
                entertain_selection = input("Please enter choice:") #eighth input
                validation_5 = gardenFunction.calculateEntertainment(entertain_selection, venue_choice) #validating entertainment selection using function in module
                input_8 = validation_5[0] #indicating state of eighth input 
                entertainment = validation_5[1] #entertainment name
                entertain_price = validation_5[2] #entertainment price 
                if input_8 == True:
                    input_7 = "correct" #breaking while loop

                else:
                    print("Wrong input, please try again") #incorrect input message

        elif entertain_choice == "2": #user doesn't want entertainment
            input_7 = "correct" #breaking loop

        else:
            print("Invalid input, please try again.") #incorrect input message


num_tables = gardenFunction.calculateTableTotal(int(people)) #calculating number of tables

calculate_1 = gardenFunction.calculateVenuePrice(venue_choice) #calculating venue price and name
venue_price = calculate_1[0] #setting variable as venue price
venue_name = calculate_1[1] #setting variable as venue name

calculate_2 = gardenFunction.calculateMenuPrice(int(num_tables), menu_selection) #calculating menu price and package name
menu_price = calculate_2[0] #setting variable as menu price
menu_package = calculate_2[1] #setting variable as package name

total = gardenFunction.calculateTotalPrice(venue_price, menu_price, entertain_price) #calculating total using function in module

textGUI.printSummaryTotal(name, number, people, num_tables, total, venue_name, menu_package, entertainment) #printing summary table using function in module


gardenFunction.booking(name, number, people, num_tables, venue_name, menu_package, entertainment) #creating text file of summary table using function in module




                                            


       


                
