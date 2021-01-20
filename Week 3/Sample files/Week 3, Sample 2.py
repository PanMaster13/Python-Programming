#Lists

list1 = [12,4.5,7,-8,0.0]
list2 = ["red","pony","blue","dagger"]
list3 = []

print(list1)
print(list2)
print(list3)

list2[1] = "JOHN CENA"
print(list2)

animals = input("Enter animals type (seperate by comma):")
list3 = animals.split(",")
print(list3)

n = int(input("N times of repeat the items in the list:"))
print(list3 * n)

        
