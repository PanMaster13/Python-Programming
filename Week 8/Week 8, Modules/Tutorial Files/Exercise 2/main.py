import menu
import calculation
import display

first_input = " "
ingre_list = "None"
course_choice = "None"
ingre_price = 0
course_price = 0

while first_input != "3":
    first_input = menu.main_menu()

    if first_input == "1":
        ingre_list = menu.ingredients()

    elif first_input == "2":
        course_choice = menu.courses()

    elif first_input == "3":
        break

    else:
        print("Invalid input, please try again.")


if ingre_list == "None":
    course_list = calculation.course_calcu(course_choice)
    course_price = course_list[0]
    course_name = course_list[1]
    total = ingre_price + course_price
    display.course_only(course_price, course_name, total)

elif course_choice == "None":
    ingre_price = calculation.ingre_calcu(ingre_list)
    total = ingre_price[0] + ingre_price[1] + ingre_price[2] + ingre_price[3] +ingre_price[4] + course_price
    display.ingre_only(ingre_price, total)
    
else:
    course_list = calculation.course_calcu(course_choice)
    course_price = course_list[0]
    course_name = course_list[1]
    ingre_price = calculation.ingre_calcu(ingre_list)
    total = ingre_price[0] + ingre_price[1] + ingre_price[2] + ingre_price[3] +ingre_price[4] + course_price
    display.ingre_course(ingre_price, course_name, course_price, total)




    
