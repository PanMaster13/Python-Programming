#Nested For Loop
row = 1
column = 1

for row in range(1,10): #outer loop
    print("Row", row)

    for column in range(1,10): #inner loop
        print("Column", column, end=' ')

    print('\n')

#Hours, Minutes and Seconds
#To find out, how many minutes and seconds in a day
h = m = s = 0


for hours in range(0,96):
    h = h + 1
    
    for minutes in range(0,60):
        m = m + 1
        
        for seconds in range(0,60):
            s = s + 1

print("Hours:", h)
print("Minutes:", m)
print("Seconds:", s)
            
            
