list1 = ["apple", "mango", "banana", "watermelon"]
list2 = ["mango", "orange", "watermelon", "kiwi"]

setx = set(list1)
sety = set(list2)

answer = setx ^ sety

print(answer)
