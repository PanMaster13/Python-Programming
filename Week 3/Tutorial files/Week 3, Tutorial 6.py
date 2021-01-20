tuplex = (4,5,7,4,4,6,8,9,2)

print("~~~~~~~~~~")

print("Values stored in tuple")

print("Tuple:", tuplex)

totalx = sum(tuplex)
maxx = max(tuplex)
minx = min(tuplex)
print("Total:", totalx)
print("Maximum:", maxx)
print("Minimum:", minx)
print("~~~~~~~~~~")

number = int(input("Enter a number:"))
n = tuplex.count(number)
print(number, "appeared", n, "times in tuple list")

             
