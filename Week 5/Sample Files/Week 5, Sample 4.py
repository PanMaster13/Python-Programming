#while and list structure
snumber = [] #empty list

num =input("Please enter numbers (separate by comma):").split(",")
snumber = num

total = i = 0

while i<len(snumber): #len(snumber) -> count the numbers inside the list
    print(snumber[i])

    total += int(snumber[i])
    i += 2

average = total/i

print("Total:", total)
print("Average:", average)
