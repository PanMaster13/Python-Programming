import menu
import display
import file
import calculate

quantity_list = menu.first_input()
price_list = calculate.calculate(quantity_list)
total = price_list[8]
print("Total:", total)

selection = file.file()

if selection == "Yes":

else:
    None
    
    
