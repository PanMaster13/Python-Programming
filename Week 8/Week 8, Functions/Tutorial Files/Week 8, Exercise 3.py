def function_3():
    ipt = input("Input a phrase:")
    listx = list(ipt)
    counter = 0
    upper = 0
    lower = 0

    list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for line in listx:
        line = listx[counter]
        if line in list1:
            upper +=1

        elif line in list2:
            lower +=1

        else:
            True

        counter +=1

    print("Number of upper case letters:", upper)
    print("Number of lower case letters:", lower)

function_3()
