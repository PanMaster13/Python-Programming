#Vowel
#Creating new strings with a FOR Loop

msg = input("Enter a message:")

new_msg = ""

vowels = "aeiou"

for letter in msg:
    if letter.lower() not in vowels:
        new_msg += letter
        print("New String:", new_msg)

print("New message without vowel:", new_msg)
