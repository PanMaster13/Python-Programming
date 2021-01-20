print("Fibonacci Series")
x = int(input("Enter the start value for Fibonacci:"))
y = int(input("Enter the end value for Fibonacci:"))

z = (x + 1)

print(x)
print(z)
opt = (x + z)

while opt <=y:
    x = z
    z = opt
    print(opt)
    opt += x
    
    
    
    
