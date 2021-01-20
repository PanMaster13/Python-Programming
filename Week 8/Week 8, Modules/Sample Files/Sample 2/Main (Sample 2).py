#Sample 2

import menu
import process
import enter
import display

print("Find out Highest or Lowest number")

c = menu.menu_option2()

while c != "3":
    if c == "1":
        n1, n2 = enter.user_input() #input
        high = process.highest(n1, n2) #process
        display.disp_highest(high) #output
        c = menu.menu_option2() #back to menu option

    if c == "2":
        n1, n2 = enter.user_input()
        low = process.lowest(n1, n2)
        display.disp_lower(low)
        c = menu.menu_option2()

    else:
        display.disp_error()
        c = menu.menu_option()

display.disp_quit()
        
