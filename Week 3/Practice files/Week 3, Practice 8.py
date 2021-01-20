list1 = ["green", "blue", "red", "purple", "white"]
list2 = ["blue", "yellow", "red", "pink", "black"]

setx = set(list1)
sety = set(list2)

opt = setx | sety

print(opt)
