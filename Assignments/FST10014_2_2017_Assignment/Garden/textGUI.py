#Function 1
def printBanner():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("|                                                     |")
    print("|                     Garden Restaurant               |")
    print("|                                                     |")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n")
    print("Welcome to Garden Restaurant Booking Management System.")
    import datetime
    today = datetime.date.today() #obtaining today's date
    print("Today's Date:", today) #printing today's date


#Function 2
def printVenue():
    print("-------------------------------------------------------")
    print(" Venue")
    print("-------------------------------------------------------")
    print("""
[1] VIP Room (10 Persons)        [4] Banquet Hall (200 persons)
[2] Executive Room (30 persons)  [5] Chamber Hall (500 persons)
[3] Pool Site (50 persons)       [6] Concert Hall (1000 persons)
           """) #printing venue option


#Function 3
def printMenuPackage():
    print("-------------------------------------------------------")
    print(" Menu Option")
    print("-------------------------------------------------------")
    print("""
[1] RM768.88 Package             [3] RM1118.88 Package
[2] RM898.88 Package             [4] RM1488.88 Package
         """) #printing menu option


#Function 4
def printPackage(menuList):
    print("-------------")
    print("Menu List")
    print("-------------")

    print("\n")

    counter = 0 #acts as an index counter
    number = 1 #number indication
    for line in menuList:
        line = menuList[counter] #obtaining item in provided list
        print(number, ".", line) #printing number and item
        counter +=1 #increasing index counter
        number +=1 #increasing number indication

    

    print("\n")

    print("Is the selected menu okay?")
    print("[1] Yes")
    print("[2] No, I want to reselect my menu") #providing option of reselecting menu


#Function 5
def printEntertainment(venueChoice, entertainmentList):
    if venueChoice == "3": #which is the pool venue
        print("Entertainment for Pool Site")
        counter = 0 #acts as an index counter
        number = 1 #number indication 
        for counter in range(0, 3):
            line = entertainmentList[counter] #obtaining item in provided list
            print(number, line) #printing number and item 
            counter +=1 #increasing index counter
            number +=1 #increasing number indication

    else:
        if venueChoice == "4": #which is the banquet hall
            print("Entertainment for Banquet Hall")
        elif venueChoice == "5": #which is the chamber hall
            print("Entertainment for Chamber Hall")
        elif venueChoice == "6": #which is the concert hall
            print("Entertainment for Concert Hall")
        else:
            None #reserved as invalid input

        counter = 1 #acts as an index counter
        number = 1 #number indication
        for counter in range(1, 5):
            line = entertainmentList[counter] #obtaining item in provided list
            print(number, line) #printing number and item
            counter +=1 #increasing index counter
            number +=1 #increasing number indication
        

#Function 6
def printSummaryTotal(custName, contNum, numPeople, totalTable, totalPrice, strVenue, strMenu, strEntertainment):
    counter = 0 #acts as index counter
    print("\n")
    print("Your reservation has been confirmed.")
    print("----------------")
    print("Booking Summary")
    print("----------------")
    list1 = ["Customer Name", "Contact Number", "No of People", "Tables", "Venue", "Package", "Add on"] #first list (for item meaning)
    list2 = [custName, contNum, numPeople, totalTable, strVenue, strMenu, strEntertainment] #second list (for item name)

    for counter in range(0, 7):
        x = list1[counter] #obtaining item in provided list
        y = list2[counter] #obtaining item in provided list
        print('{:14}: {}'.format(x, y)) #formated to ensure that it is printed in unity (14 spaces)
        counter +=1 #increasing index counter

    print("\n")
    print("Total Price:", totalPrice) #displaying total price

    


