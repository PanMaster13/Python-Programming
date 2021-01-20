studentname = []
studentmarks = []

names = input("Enter student's names (separated by using commas):").split(",")
marks = input("Enter student's marks (separated by using commas):").split(",")
total = 0
studentname = names
studentmarks = marks

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Excellent Tuition Center")

x = len(names)
y = len(marks)

while x >0 and y >0:
    x -=1
    y -=1
    mark = int(marks[y])
    total = (total + mark)
    if mark < 50:
        grade = "Fail"
    elif ((mark >= 50) and (mark <= 65)):
        grade = "Pass"
    elif ((mark >= 66) and (mark <= 75)):
        grade = "Credit"
    else:
        grade = "Distinction"
    print("Student Name:", names[x], "\t", "Marks:", marks[y], "\t", "Grade:", grade)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
z = len(marks)
average = (total / z)
print("Total Marks:", total)
print("Average Marks:", average)
    
