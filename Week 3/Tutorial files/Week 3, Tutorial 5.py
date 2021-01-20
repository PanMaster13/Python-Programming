dict1 = {1000145:85.5, 1000159:77, 1000258:61.5, 1000112:55.8}

marks1 = dict1.values()

total1 = sum(marks1)

average1 = (total1 / 4)

print("Original List:", dict1)
print("Total:", total1)
print("Average:", average1)

dict1["1000147"] = 61.5
dict1["1000588"] = 55
print("\n")

marks2 = dict1.values()

total2 = sum(marks2)

average2 = (total2 / 6)

print("After update:", dict1)
print("Total", total2)
print("Average", average2)
