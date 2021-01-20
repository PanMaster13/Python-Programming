ipt = input("Enter numbers *Separate by commas:").split(",")

print("~~Output~~")
over_10 = []
below_10 = []
x = totalx = totaly = 0

for items in ipt:
    a = int(ipt[x])
    x +=1

    if a >= 10:
        over_10.append(a)
        totalx = totalx + a
    elif a < 10:
        below_10.append(a)
        totaly = totaly + a
    else:
        print("Wrong input")

totalx = totalx * 1.5
totaly = totaly * 2
print("Values >=10:", over_10)
print("Values < 10:", below_10)
print("Total for values >= 10:", totalx)
print("Total for values <  10:", totaly)

even_value = []
odd_value = []

y = 0
for items in ipt:
    a = int(ipt[y])
    y +=1

    if a % 2:
        odd_value.append(a)

    else:
        even_value.append(a)

even_num = len(even_value)
odd_num = len(odd_value)
print("Numbers of Even values:", even_num)
print("Numbers of Odd values:", odd_num)
print("Even values:", even_value)
print("Odd values:", odd_value)
total = totalx + totaly
print("Total:", total)
