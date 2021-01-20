#Sample8.py - rename and remove text file

import os #import operating system module file

file = open("testing.txt","w")

file.write("1")

file.close()

#Rename
os.rename("testing.txt","t.txt")

#Delete
#os.remove("t.txt")
