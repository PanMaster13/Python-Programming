#Random access
#String indexing

import random
word = input("Enter a word:")

print("Programming Language:", word, "\n")

high_len = len(word)
low_len = -len(word)

print("Higher Length:", high_len)
print("Lower Length:", low_len)

for i in range(15):
    position = random.randrange(low_len,high_len)
    print("Word [", position, "]\t", word[position])
    
