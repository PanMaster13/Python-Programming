def ingre_calcu(ingre_list):
    cost_1 = (ingre_list[0] * 4.50)
    cost_2 = (ingre_list[1] * 6.59)
    cost_3 = (ingre_list[2] * 12.50)
    cost_4 = (ingre_list[3] * 4.99)
    cost_5 = (ingre_list[4] * 0.16)

    return cost_1, cost_2, cost_3, cost_4, cost_5

def course_calcu(choice):
    if choice == "4":
        price = float(450)
        course = "4 Days DIY Soap Course"

    elif choice == "5":
        price = float(550)
        course = "5 Days DIY Soap Course"

    else:
        price = float(650)
        course = "6 Days DIY Soap Course"

    return price, course




    

    
