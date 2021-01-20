from decimal import Decimal

int_num = int(input("Initial number:"))
end_num = int(input("Ending number:"))
x_num = int(input("Decreasing number:"))

num_total = num_counter = 0
if int_num < end_num:
    int_num,end_num = end_num,int_num

x_num = (x_num*-1)

for int_num in range(int_num,end_num,x_num):
    print(int_num)
    num_total = (num_total + int_num)
    num_counter +=1


num_average = round(num_total/num_counter, 2)

print("Total:", num_total)
print("Average:", num_average)
