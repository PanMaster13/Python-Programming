#Sample6.py

def fileRead(fname):
    with open(fname) as file:
        #content_list is the list that contains the read lines
        content_list = file.readlines()
        print(content_list)

fileRead("write.txt")
