#random access sample

import random

word = 'index'
print('The word is: {}'.format(word))

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low,high)
    print("Word [{}] \t {}".format(position, word[position]))

input('Enter to exit')
print('\n\n')

#no vowels sample
message = input('Enter a message:')
newMessage = ""
vowels = 'aeiou'

for letter in message:
    if letter.lower() not in vowels:
        newMessage += letter
        print('A new string has been created: {}'.format(newMessage))

input('Enter to exit')


#count total even and odd numbers
numbers =(1,2,3,4,5,6,7,8,9)
countOdd = 0
countEven = 0
for i in numbers:
    if i%2 == 0:
        countEven += 1
    else:
        countOdd += 1

print('Even numbers : {}'.format(countEven))
print('Odd numbers : {}'.format(countOdd))

#nested loop example
row = 1
column = 1

for row in range(1,10):
    print(row)

    for column in range(1,10):
        print(column, end=' ')

    print('\n')
