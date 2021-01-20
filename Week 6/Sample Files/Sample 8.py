#Iterating over List

print("Iterating over List")

data_list = (123, 456.78, True, "Python", (0,1), [18,12], {"Subject":"Python", "Group":"2"})

for item in data_list:
    print("Type of ", item, "is", type(item))

print("\nFor Loop and Dictionary")
color_dict = {"C1":"Red", "C2":"Blue", "C3":"White", "C4":"Black"}
print("Display the keys")
for c in color_dict: #display the keys
    print(c)

print("\nDisplay the values")
for colorvalue in color_dict.values():
    print(colorvalue)
