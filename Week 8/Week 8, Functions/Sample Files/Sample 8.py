#Sample 8
print("\n")

n = 789
def num():
    print(n)
    global abc
    abc = 123
    print(abc)

num()
print(abc)
