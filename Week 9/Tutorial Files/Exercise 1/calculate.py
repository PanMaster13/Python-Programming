def calculate():
    file = open("Number List.txt","r")

    x = file.readline()
    list1 = x.split(",")
    limit = len(list1)
    counter = 0
    total = 0
    while counter < limit:
        total = int(total) + int(list1[counter])
        counter +=1
    

    average = total/limit

    print("Total:", total)
    print("Average:", average)
