#Tuples
tup1 = (12,-8,2.5,-12.22,8,0.5) #numeric
tup2 = ("red","Pink","white","blue") #string
tup3 = "Amy Ling", 56; #Mix data types

print(tup1)
print(tup2)
print(tup3)

tup4 = ()
print(tup4)

print(tup1[2])
#print(tup2[5]) (Output: Index out of range)

print(tup1[1:4])
#tup2[3] = "black" (Error: tuple is immutable)

# + operator (Join several tuples)
# * operator (Repeat the tuple to n times)

t1 = (1,4,7)
t2 = (10,7,4)
t3 = (2,6,9)

print(t3 + t2)
print(t1 * 4)
