#Read file with function in python - fread2.py

def readFile(fname):
    file = open(fname)
    print(file.read())

readFile("write.txt")
