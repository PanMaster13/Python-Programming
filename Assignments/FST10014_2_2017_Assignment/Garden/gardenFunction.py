#Function 1
def readVenueList(textFile):
    #Creating empty dictionaries
    dict1 = {"name":"", "max":"", "cost":""}
    dict2 = {"name":"", "max":"", "cost":""}
    dict3 = {"name":"", "max":"", "cost":""}
    dict4 = {"name":"", "max":"", "cost":""}
    dict5 = {"name":"", "max":"", "cost":""}
    dict6 = {"name":"", "max":"", "cost":""}

    #Opening files
    with open(textFile,"r") as x:
        data1 = x.readlines(1)
        data2 = x.readlines(2)
        data3 = x.readlines(3)
        data4 = x.readlines(4)
        data5 = x.readlines(5)
        data6 = x.readlines(6)

    #Creating lists
    list1 = (data1[0]).split(",")
    list2 = (data2[0]).split(",")
    list3 = (data3[0]).split(",")
    list4 = (data4[0]).split(",")
    list5 = (data5[0]).split(",")
    list6 = (data6[0]).split(",")

    #Updating dictionary 1
    dict1.update({"name":list1[0]})
    dict1.update({"max":list1[1]})
    dict1.update({"cost":list1[2]})

    #Updating dictionary 2
    dict2.update({"name":list2[0]})
    dict2.update({"max":list2[1]})
    dict2.update({"cost":list2[2]})

    #Updating dictionary 3
    dict3.update({"name":list3[0]})
    dict3.update({"max":list3[1]})
    dict3.update({"cost":list3[2]})

    #Updating dictionary 4
    dict4.update({"name":list4[0]})
    dict4.update({"max":list4[1]})
    dict4.update({"cost":list4[2]})

    #Updating dictionary 5
    dict5.update({"name":list5[0]})
    dict5.update({"max":list5[1]})
    dict5.update({"cost":list5[2]})

    #Updating dictionary 6
    dict6.update({"name":list6[0]})
    dict6.update({"max":list6[1]})
    dict6.update({"cost":list6[2]})

    return dict1, dict2, dict3, dict4, dict5, dict6

#Function 2
def validateCustomerName(name):
    if any(number.isdigit() for number in name) or len(name.split(" "))!=2: #to detect whether the given name has string numbers or the given name is more than 2
        return False
    else: #this means the given name passes validation
        return True
       

#Fuction 3
def validateNoOfPeople(people):
    if (people.isdigit()) and ((int(people) >=1) and (int(people)) <=1000): #to detect whether the given number of people is in number and the number is within 1 to 1000
        people = int(people) #makes the input into a integer
        return people
    else:
        return -1 #to indicate that it is false


#Fuction 4
def validatePhoneNumber(number):
    if (number.isdigit()) and (len(number)==10): #to detect whether the given input is numeric and it has 10 characters
        return True #passes validation
    else:
        return -1 #to indicate that it is false


#Function 5
def validateVenue(choice, venueList, noPeople):
    if choice =="1":
        venue_dict = venueList[0] #extracts first dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation

    elif choice =="2":
        venue_dict = venueList[1] #extracts second dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation
        
    elif choice =="3":
        venue_dict = venueList[2] #extracts third dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation


    elif choice =="4":
        venue_dict = venueList[3] #extracts fourth dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation


    elif choice =="5":
        venue_dict = venueList[4] #extracts fifth dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation

    elif choice =="6":
        venue_dict = venueList[5] #extracts sixth dictionary list from the list
        if noPeople > int(venue_dict["max"]): #to determine the limit based on the given venue
            return False #fails validation
        else:
            return True #passed validation


    else:
        print("") #prints empty space if all the conditions don't meet


#Function 6
def readitemList(textFile):
    with open(textFile, "r") as (file_1): #opens text file based on given name
        list1 = file_1.readlines() #reads the text file into a list
        list1 = [x.strip() for x in list1] #strips the items in the list
    
    return list1 #returns the list

          
#Function 7
def calculateTableTotal(noPeople):
    num_table = noPeople//10 #calculates the initial number of tables
    if (noPeople%10) > 5: #determining whether the remainder of the calculation is more than five
        num_table +=1 #adds in an extra table
        return num_table
    else:
        return num_table #returns initial number of tables
    


#Function 8
def calculateVenuePrice(venueChoice):
    venue_list = readVenueList("venue.txt") #reads the venue text file
    if venueChoice == "1":
        venue_dict = venue_list[0] #selects first dictionary from list
        venue_price = float(venue_dict["cost"]) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    elif venueChoice == "2":
        venue_dict = venue_list[1] #selects second dictionary from list
        venue_price = float(venue_dict["cost"]) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    elif venueChoice == "3":
        venue_dict = venue_list[2] #selects third dictionary from list
        venue_price = float(venue_dict["cost"] ) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    elif venueChoice == "4":
        venue_dict = venue_list[3] #selects fourth dictionary from list
        venue_price = float(venue_dict["cost"]) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    elif venueChoice == "5":
        venue_dict = venue_list[4] #selects fifth dictionary from list
        venue_price = float(venue_dict["cost"]) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    elif venueChoice == "6":
        venue_dict = venue_list[5] #selects sixth dictionary from list
        venue_price = float(venue_dict["cost"]) #cost of selected venue
        selected_venue = venue_dict["name"] #name of selected venue

    else:
        return False #indicating invalid input

    return venue_price, selected_venue #returns cost and name of venue


#Function 9
def calculateMenuPrice(totalTable, choice):
    if choice == "1":
        menu_price = float(totalTable * 768.88) #calculating menu price
        package = "RM768.88 Package" #indicating which menu by package name

    elif choice == "2":
        menu_price = float(totalTable * 898.88) #calculating menu price
        package = "RM898.88 Package" #indicating which menu by package name

    elif choice == "3":
        menu_price = float(totalTable * 1118.88) #calculating menu price
        package = "RM1118.88 Package" #indicating which menu by package name

    elif choice == "4":
        menu_price = float(totalTable * 1488.88) #calculating menu price
        package = "RM1488.88 Package" #indicating which menu by package name

    else:
        False #indicating invalid input
        
    return menu_price, package #returns price and name of menu


#Function 10
def calculateEntertainment(choice, venueChoice):
    entertainment = "None" #initial type of entertainment (No entertainment)
    entertain_price = float(0) #initial cost of entertainment (No entertainment)
    
    if venueChoice == "3": #which is the pool venue

        if choice == "1": #Synchronised Swimming Dance entertainment
            validation = True #to pass the validation
            entertainment = "Synchronised Swimming Dance" #name of entertainment
            entertain_price = float(2000) #cost of entertainment

        elif choice == "2": #Clown Performance entertainment
            validation = True #to pass the validation
            entertainment = "Clown Performance" #name of entertainment
            entertain_price = float(250) #cost of entertainment

        elif choice == "3": #Magic Performance entertainment
            validation = True #to pass the validation
            entertainment = "Magic Performance" #name of entertainment
            entertain_price = float(400) #cost of entertainment

        else:
            validation = False #failed validation

    elif venueChoice == "4" or venueChoice == "5" or venueChoice == "6": #which are the banquet hall, chamber hall and concert hall venue

        if choice == "1": #Clown Performance entertainment
            validation = True #to pass the validation
            entertainment = "Clown Performance" #name of entertainment
            entertain_price = float(250) #cost of entertainment

        elif choice == "2": #Magic Performance entertainment
            validation = True #to pass the validation
            entertainment = "Magic Performance" #name of entertainment
            entertain_price = float(400) #cost of entertainment

        elif choice == "3": #House Dance Performance entertainment
            validation = True #to pass the validation
            entertainment = "House Dance Performance" #name of entertainment
            entertain_price = float(1000) #cost of entertainment
 
        elif choice == "4": #Live Band Performance entertainment
            validation = True #to pass the validation
            entertainment = "Live Band Performance" #name of entertainment
            entertain_price = float(1500) #cost of entertainment

        else:
            validation = False #failed validation

    else:
        validation = False #failed validation

    return validation, entertainment, entertain_price


#Function 11
def calculateTotalPrice(venuePrice, menuPrice, entertainmentPrice):
    total = venuePrice + menuPrice + entertainmentPrice #calculating the total price
    total = round(total, 2) #rounding the total to 2 decimals

    return total

#Function 12
def booking(custName, custNo, noPeople, totaltable, strVenue, strMenu, strEntertainment):
    import datetime
    today = datetime.date.today() #making today's date

    file_custName = custName.split(" ") #splitting the name into 2, allowing to obtain given name only
    filename = "booking/" + file_custName[0] + "_" + str(today.year) + str(today.month) + str(today.day) + ".txt" #destination and name of text file created by adding strings
    file = open(filename, "w") #opening and writing the text file

    file.write("""
----------------
Booking Summary
----------------
Customer Name : {}
Contact Number: {}
No of People  : {}
Tables        : {}
Venue         : {}
Package       : {}
Add on        : {}
""".format(str(custName), str(custNo), str(noPeople), str(totaltable), str(strVenue), str(strMenu), str(strEntertainment))) #.format to place strings into the desired {} slot

    file.close() #closing file
