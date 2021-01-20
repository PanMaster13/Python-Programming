#Week 4 Samples 

#Single-alternative
#if<condition>
        #Then<True>

#Dual-Alternative
#if<condition>
        #Then<True>
        #Else<False>

#Single alternative
#Sample 1
print("Single alternative")

#a = 10
a = int(input("Enter a value:")) #must have int because without it the numbers are only string.
if (a>=10): #condition #comparing numeric number
    print("Value", a, "is greater or equal than 10") #True action

