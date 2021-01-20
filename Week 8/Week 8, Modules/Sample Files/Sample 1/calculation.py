#Sample 1
#Calculation Module

def calc_Add(n1, n2):
    total = n1 + n2
    return total

def calc_sub(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    total = n1 - n2
    return total
