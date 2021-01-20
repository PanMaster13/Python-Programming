#Decrease loop by using input value
#Calculate and display total and average

initial_v = int(input("Initial value:"))
ending_v = int(input("Ending value:"))
decrease_v = int(input("Decrease Value:"))

total = cnt = 0

for a in range(initial_v,ending_v,decrease_v):
    print(a)
    total = total + a #(total+=a)
    cnt = cnt + 1 #counter

print("Total:", total)
print("Average:", total/cnt)

