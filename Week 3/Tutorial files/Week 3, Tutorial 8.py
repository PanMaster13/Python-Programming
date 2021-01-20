list1 = []
color_set = set(list1)

color_set.add("white")
color_set.add("pink")
color_set.add("black")

print(color_set)

user_input = input("Add color names into the list:")
user_input1 = user_input.split(",")
color_set.update(user_input1)

print(color_set)

user_discard = input("Name color to be discarded:")

color_set.discard(user_discard)

print(color_set)

