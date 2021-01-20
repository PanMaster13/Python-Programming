dog_age = int(input("Input a dog's age in human years:"))

if dog_age < 0:
    print("Input must be more than 0")

if dog_age <= 2:
    answer = (dog_age) * 10.5

if dog_age > 2:
    answer = 21 + ((dog_age - 2) * 4)
print("The dog's age in dog's years is", answer)
