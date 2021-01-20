#Sample 3

print("Simple Mathematical calculator")
print("""
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
""")

s = (input("Enter your selection:"))

n1 = float(input("Enter first number:"))
n2 = float(input("Enter second number:"))

if s =="1":
    ans = n1 + n2
elif s =="2":
    if n1 < n2:  #nestedif
        n1,n2 = n2,n1
        ans = n1 - n2
elif s =="3":
    ans = n1 * n2
elif s =="4":
    if n1 < n2:  #nestedif
        n1,n2 = n2,n1
    ans = n1 / n2
else:
    print("Wrong input")

print("Answer:", ans)
