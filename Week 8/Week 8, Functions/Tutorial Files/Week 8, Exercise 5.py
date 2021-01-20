def function_5():
    ipt = input("Enter numbers *separate by commas:").split(",")

    counter = 0
    even_list = []
    odd_list = []
    limit = len(ipt)

    for counter in range(0, limit):
        if (float(ipt[counter])%2) == 0:
            even_list.append(ipt[counter])

        else:
            odd_list.append(ipt[counter])

        counter +=1


    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)


function_5()
            
