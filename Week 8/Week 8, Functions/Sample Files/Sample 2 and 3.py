#Sample 2
import display
def calc_avg(x, y): #function: calc_avg
    avg = (x + y)/2
    print("Average:", avg)

calc_avg(12,25) #calling the function with arg values


#Sample 3



c = print(""""
[1]Function tutorial
[2]Module tutorial
""")

c = input("Choice:")

if c == "1":
    display.printmsg1() #Module
elif c == "2":
    display.printmsg2()
else:
    display.printerror()


