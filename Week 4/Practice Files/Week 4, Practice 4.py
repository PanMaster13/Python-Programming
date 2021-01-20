x = int(input("Input the length of side1:"))
y = int(input("Input the length of side2:"))
z = int(input("Input the length of side3:"))

if x + y > z and x + z > y and y + z > x:
    print("The triangle is valid")

else:
    print("The triangle is not valid")
    
