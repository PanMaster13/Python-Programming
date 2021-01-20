#Tuple - iterating over tuple
from decimal import Decimal

num = (1,2,3,4,5,6,7,8,21,18,19,54,74)

#count Odd and Even numbers
c_odd = c_even = t_odd = t_even = 0

for x in num:
    if x % 2:
        c_odd += 1
        t_odd += x
    else:
        c_even += 1
        t_even += x

print("Number of Even numbers:", c_even)
print("Total of Even numbers:", t_even)
print("Average of Even numbers:", round(t_even/c_even,2))
print("Number of Odd numbers:", c_odd)
print("Total of Odd numbers:", t_odd)
print("Average of Odd numbers:", round(t_odd/c_odd,2))
