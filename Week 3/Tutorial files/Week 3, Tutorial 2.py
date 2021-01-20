Title = ["Student ID","Student Name","Marks","Grade"]

Student1 = []
Student2 = []
Student3 = []

print("Enter Student ID, Student Name, Marks and Grade (separate with comma)")


inpt1 = input("Student 1:")
inpt2 = input("Student 2:")
inpt3 = input("Student 3:")

Students1 = inpt1.split(",")
Students2 = inpt2.split(",")
Students3 = inpt3.split(",")
A = list(Title)
B = list(Students1)
C = list(Students2)
D = list(Students3)

from random import shuffle
ans1 = shuffle(A)
ans2 = shuffle(B)
ans3 = shuffle(C)
ans4 = shuffle(D)
print(ans1,ans2,ans3,ans4)




