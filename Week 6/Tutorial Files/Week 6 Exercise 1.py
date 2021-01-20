n = 1
n_odd = n_even = 0

for n in range(1,101,1):
    if n % 2:
        n_odd += n

    else:
        n_even += n

print("Total for even numbers:", n_even)
print("Total for odd numbers:", n_odd)

