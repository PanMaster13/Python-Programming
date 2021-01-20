#Read file with append: fread3.py

file = open("write.txt", "r")

myList = []

for line in file:
    myList.append(line)

print(myList)
print(myList[0])

file.close()
