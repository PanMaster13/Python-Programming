#Sample 4

def total(n1, n2=3):
    total = n1 + n2
    return total

print("Total:", total(12))
print("Total:", total(12,25))

print("\n\n")

#Sample 5
def studMarks(IT, Programming = 60, Maths = 50):
    print("~~Marks~~")
    print("IT:", IT)
    print("Programming:", Programming)
    print("Maths:", Maths)
    print("\n")
    
studMarks(78,79)
studMarks(77, Maths = 65)
studMarks(78,79,80)

