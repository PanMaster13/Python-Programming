import re

print("""Input a password with the following traits:
    - At least 1 letter between [a-z] and 1 letter between [A-Z]
    - At least 1 number between [0-9]
    - At least 1 character from [$#@]
    - Minimum length 6 characters
    - Maximum length 16 characters
    """)

password = input("Password:")
p_word_valid = True

while p_word_valid:
    if ((len(password) <6) or (len(password) >=16)):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif not re.search("\s", password):
        break
    else:
        print("Valid password")
        

if p_word_valid:
    print("Invalid password")
    
    
