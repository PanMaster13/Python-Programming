ipt = input("Enter numbers *Separate by using commas:").split(",")

print("**Output**")

print("List:", ipt)

numbers = len(ipt)

print("Numbers entered:", numbers)

total = x = 0
for items in ipt:
    a = int(ipt[x])
    total = total + a
    x +=1

average = (total / numbers)
print("Total:", total)
print("Average:", average)

    
