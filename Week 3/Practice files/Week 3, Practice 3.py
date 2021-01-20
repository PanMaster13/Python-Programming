list1 = ["Winter","Summer","Autumn"]
list2 = ["Winter","Spring"]
list3 = ["Spring"]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

answer = set1-set2-set3

print(answer)
