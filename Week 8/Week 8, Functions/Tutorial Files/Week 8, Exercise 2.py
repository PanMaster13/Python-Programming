def function_2():
    print("User input")
    ipt = input("What's your message?")

    list1 = []
    counter = 1

    for i in range(0, len(ipt)):
        list1.append(ipt[len(ipt)-counter])
        counter +=1

    list1 = "".join(list1)

    print("\n~Output")
    print("Message in reverse order:", list1)


function_2()
