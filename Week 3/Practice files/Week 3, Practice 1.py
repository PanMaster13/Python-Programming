list_1 = [12,8,9,2.5,3.6,7,4.4,14.5]
list_2 = [2.5,3,14.5,12,9]

set_1 = set(list_1)
set_2 = set(list_2)

print("List1 is given", list_1)
print("List2 is given", list_2)
print("Output 1:", set_1-set_2)
print("Output 2:", set_2-set_1)
