print("Scrabble Game")
word = list(input("Enter a word:"))

counter = total = 0
print("*********************************")
print("*Letter \t*Score \t\t*")
    
for x in word:
    x = word[counter].lower()
    if x =="a":
        point = 1
        
    elif x =="b":
        point = 3
        
    elif x =="c":
        point = 3
        
    elif x =="d":
        point = 1
        
    elif x =="e":
        point = 2
        
    elif x =="f":
        point = 2
        
    elif x =="g":
        point = 4
        
    elif x =="h":
        point = 1
        
    elif x =="i":
        point = 4
        
    elif x =="j":
        point = 5
        
    elif x =="k":
        point = 8
        
    elif x =="l":
        point = 3
        
    elif x =="m":
        point = 1
        
    elif x =="n":
        point = 1
        
    elif x =="o":
        point = 1
        
    elif x =="p":
        point = 10
        
    elif x =="q":
        point = 3
        
    elif x =="r":
        point = 1
        
    elif x =="s":
        point = 1
        
    elif x =="t":
        point = 1
        
    elif x =="u":
        point = 1
        
    elif x =="v":
        point = 4
        
    elif x =="w":
        point = 4
        
    elif x =="x":
        point = 4
        
    elif x =="y":
        point = 8
        
    elif x =="z":
        point = 10

    total = (total + point)
    print("*", x, "\t\t*", point, "\t\t*")
    print("*********************************")
    counter = (counter + 1)

print("Total:", total)
