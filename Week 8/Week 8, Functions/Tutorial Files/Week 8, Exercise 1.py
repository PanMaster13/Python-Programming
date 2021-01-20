def function_1():
    print("User input")
    num_1 = float(input("First number:"))
    num_2 = float(input("Second number:"))
    num_3 = float(input("Third number:"))

    list1 = [num_1, num_2, num_3]

    largest = max(list1)
    smallest = min(list1)

    print("\n~Output~")
    print("Largest:", largest)
    print("Smallest:", smallest)

function_1()
    
