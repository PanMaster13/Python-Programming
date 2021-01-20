#Increase loop by using input value
#Calculate and display total and average

initial_v = int(input("Initial value:"))
ending_v = int(input("Ending value:"))
increase_v = int(input("Increase Value:"))

total = cnt = 0

for a in range(initial_v,ending_v,increase_v):
    print(a)
    total = total + a #(total+=a)
    cnt = cnt + 1 #counter

print("Total:", total)
print("Average:", total/cnt)

