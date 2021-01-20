months = input("Enter 12 months (separate with comma):") 

denied = input("Enter a month to be removed from the list:") 

x = months.split(',')

y = denied.split(',')

set1 = set(x) 

set2 = set(y) 


print(set2, "will be removed from the list") 

opt = set1 ^ set2 

print("New List:", opt) 

