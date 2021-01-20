#Using input statement
#increase loop
n = 10
endloop = int(input("Enter a value to end the loop:"))
increase = int(input("Enter a value to increase the loop:"))

while n <= endloop:
    print(n)
    n += increase


#string input
response = ""
while response != "good": #!= is not
    response = input("How are you:")

print("Good!")

    
              
