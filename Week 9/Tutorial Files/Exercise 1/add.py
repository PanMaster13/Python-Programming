def adding():
    number_list = input("Enter numbers (separate with comma):")

    file = open("Number List.txt","w")
    file.write(number_list)

    file.close()
