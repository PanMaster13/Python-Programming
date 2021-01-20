import random
print("~~Number Guessing Game~~")
num_range = int(input("Enter a number range for the game:"))
n = int(random.randint(1, num_range))
new_num = int(input("New number:"))

              

while new_num != n:
    if new_num > n:
        print("Number too large")
        number = int(input("New number:"))

    elif new_num < n:
        print("Number too small")
        number = int(input("New number:"))

    else:
        print("Congratulations. You made it!")
        break
    
