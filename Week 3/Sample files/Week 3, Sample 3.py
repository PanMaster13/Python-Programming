#Sets

a = [2,5,9,36,1,2,4,2,4,6,7,2.5,3.6]
b = [12,9,2,36,-12,56,3.5,4.7]

s1 = set(a)
s2 = set(b)

print(s1)
print(s2)

print("Numbers in Set1 but not Set2:", s1 - s2)
print("Numbers in Set2 but not Set1:", s2 - s1)

print("Numbers in either Set1 or Set2:", s1 | s2)
print("Numbers in both Set1 and Set2:", s1 & s2)
print("Numbers in either Set1 or Set2 but not both:", s1 ^ s2)

s2.add(88)
print(s2)
#.add, .update, .discard

