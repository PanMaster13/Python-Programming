#line.split - sample5.py

with open("write.txt", "r") as file: #same as "file = open("write.txt", "r")"
    rfile = file.readlines()


for line in rfile:
    words = line.split()
    print(words)
    print(words[0])
    
print(words)

file.close()
