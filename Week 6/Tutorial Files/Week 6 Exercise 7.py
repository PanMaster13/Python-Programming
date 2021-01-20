print("~Find and Replace~")
ipt = input("Enter a phrase:")
remove = input("Enter a letter to find:")
replace = input("Enter a letter to replace:")
new_ipt = ipt.replace(remove, replace)
print("New phrase:", new_ipt)

x = counter = y = 0
list_ipt = list(ipt)
position = []

for item in list_ipt:
    a = list_ipt[x]
    x +=1
    if a == remove:
        counter +=1
        position += "~" + str(x)


print(remove, "appeared", counter, "times in the phrase")
print(remove, "appeared at position:", "".join(position))

