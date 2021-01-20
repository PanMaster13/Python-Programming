#Sample 6

def sum(*num):
    x = 0
    for n in num:
        print(n, "N in numbers:", x)
        x += n

    return x

print("Total:", sum(2,4,6,8,10))
