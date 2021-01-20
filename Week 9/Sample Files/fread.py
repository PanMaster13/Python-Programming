#Read file om python - fread.py

file = open("write.txt", "r")

#Remone # for effect

#print(file.read()) #read and print all characters
#print(file.read(10)) #read and print first 10 characters including spacing
print(file.readline()) #read and print first line


file.close()

