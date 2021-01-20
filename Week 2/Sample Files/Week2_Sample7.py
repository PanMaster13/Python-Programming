#Global Variable
sub1 = "Python"

#Create a function
def func1():
    global sub1
    sub1 = "PHP"
    print("Subject:", sub1)

def func2():
    print("Subject:", sub1)
    
    
#Call the function
func1()
func2()
