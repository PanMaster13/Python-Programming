x = int(input("Input first number:"))
y = int(input("Input second number:"))
z = int(input("Input third number:"))

if ((x <= y) and (z <= x)) or ((x <= z) and (y <= x)):
    print("The median is", x)

elif ((y <= z) and (x <= y)) or ((y <= x) and (z <= y)):
    print("The median is", y)

elif ((z <= x) and (y <= z)) or ((z <= y) and (x <= z)):
    print("The median is", z)

else:
    print("Invalid input")
    

        
