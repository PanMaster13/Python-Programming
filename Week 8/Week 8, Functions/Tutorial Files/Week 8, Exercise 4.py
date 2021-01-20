def function_4():
    name_list = input("Enter name *Separate by commas:").split(",")
    mark_list = input("Enter marks *Separate by commas:").split(",")

    counter = 0
    limit = len(mark_list)
    total_mark = 0

    print("\n~Output")
    for counter in range(0, limit):
        print("Student Name:", name_list[counter], "\t| Marks:", mark_list[counter])
        total_mark = total_mark + int(mark_list[counter])
        counter +=1

    average_mark = total_mark/limit
    print("Total of", limit, "students' marks is:", total_mark)
    print("Average is:", average_mark)

function_4()
