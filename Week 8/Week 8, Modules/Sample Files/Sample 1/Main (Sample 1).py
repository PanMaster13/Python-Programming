#Sample 1
#Main file

import menu
import calculation
import display
import enter

c = menu.menu_option()




while c != "3":
    if c == "1":
        n1, n2 = enter.user_input()
        ans = calculation.calc_Add(n1, n2)
        display.disp_ans(ans)
        c = menu.menu_option()

    elif c == "2":
        n1, n2 = enter.user_input()
        ans = calculation.calc_sub(n1, n2)
        display.disp_ans(ans)
        c = menu.menu_option()

    else:
        display.disp_error()
        c = menu.menu_option()

display.disp_quit()
