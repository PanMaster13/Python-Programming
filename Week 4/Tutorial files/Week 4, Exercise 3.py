from decimal import Decimal
import math
print("Excellent Tuition Center")
name = input("Student Name:")
num_sub = input("Number of subjects (3/5):")
if num_sub == "3":
    sub1 = input("Subject 1:")
    mark1 = float(input("Marks:"))

    sub2 = input("Subject 2:")
    mark2 = float(input("Marks:"))

    sub3 = input("Subject 3:")
    mark3 = float(input("Marks:"))
    
    

    if mark1 < 50:
        grade1 = "Fail"

    elif ((mark1 >= 50) and (mark1 <= 65)):
        grade1 = "Pass"

    elif ((mark1 >= 66) and (mark1 <= 75)):
        grade1 = "Credit"

    elif ((mark1 > 75) and (mark1 <= 100)):
        grade1 = "Distinction"

    else:
        print("Wrong input")

    if mark2 < 50:
        grade2 = "Fail"

    elif ((mark2 >= 50) and (mark2 <= 65)):
        grade2 = "Pass"

    elif ((mark2 >= 66) and (mark2 <= 75)):
        grade2 = "Credit"

    elif ((mark2 > 75) and (mark2 <= 100)):
        grade2 = "Distinction"

    else:
        print("Wrong input")

    if mark3 < 50:
        grade3 = "Fail"

    elif ((mark3 >= 50) and (mark3 <= 65)):
        grade3 = "Pass"

    elif ((mark3 >= 66) and (mark3 <= 75)):
        grade3 = "Credit"

    elif ((mark3 > 75) and (mark3 <= 100)):
        grade3 = "Distinction"

    else:
        print("Wrong input")

    list1 = [mark1,mark2,mark3]
    high_mark = max(list1)
    low_mark = min(list1)
    if mark1 == high_mark:
        high_sub = sub1

    elif mark2 == high_mark:
        high_sub = sub2

    elif mark3 == high_mark:
        high_sub = sub3

    else:
        print("Wrong input")

    if mark1 == low_mark:
        low_sub = sub1

    elif mark2 == low_mark:
        low_sub = sub2

    elif mark3 == low_marks:
        low_sub = sub3

    else:
        print("Wrong input")
        
    
        
    total = (mark1 + mark2 + mark3)
    average = total / 3
    if average < 50:
        over_grade = "Fail"

    elif ((average >= 50) and (average <= 65)):
        over_grade = "Pass"

    elif ((average >= 66) and (average <= 75)):
        over_grade = "Credit"

    elif ((average > 75) and (average <= 100)):
        over_grade = "Distinction"

    else:
        print("Wrong input")
    x = round(average,2)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Subject 1:", sub1, "\t", "\t", "Mark:", mark1, "\t", "Grade:", grade1)
    print("Subject 2:", sub2, "\t", "\t", "Mark:", mark2, "\t", "Grade:", grade2)
    print("Subject 3:", sub3, "\t", "\t", "Mark:", mark3, "\t", "Grade:", grade3)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Highest Marks:", high_mark, "\t", "\t", "Subject:", high_sub)
    print("Lowest Marks:", low_mark, "\t", "\t", "Subject:", low_sub)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Marks:", total)
    print("Average Marks:", x)
    print("Overall Grade:", over_grade)
    

elif num_sub == "5":
    sub1 = input("Subject 1:")
    mark1 = float(input("Marks:"))

    sub2 = input("Subject 2:")
    mark2 = float(input("Marks:"))

    sub3 = input("Subject 3:")
    mark3 = float(input("Marks:"))

    sub4 = input("Subject 4:")
    mark4 = float(input("Marks:"))

    sub5 = input("Subject 5:")
    mark5 = float(input("Marks:"))

    if mark1 < 50:
        grade1 = "Fail"

    elif ((mark1 >= 50) and (mark1 <= 65)):
        grade1 = "Pass"

    elif ((mark1 >= 66) and (mark1 <= 75)):
        grade1 = "Credit"

    elif ((mark1 > 75) and (mark1 <= 100)):
        grade1 = "Distinction"

    else:
        print("Wrong input")

    if mark2 < 50:
        grade2 = "Fail"

    elif ((mark2 >= 50) and (mark2 <= 65)):
        grade2 = "Pass"

    elif ((mark2 >= 66) and (mark2 <= 75)):
        grade2 = "Credit"

    elif ((mark2 > 75) and (mark2 <= 100)):
        grade2 = "Distinction"

    else:
        print("Wrong input")

    if mark3 < 50:
        grade3 = "Fail"

    elif ((mark3 >= 50) and (mark3 <= 65)):
        grade3 = "Pass"

    elif ((mark3 >= 66) and (mark3 <= 75)):
        grade3 = "Credit"

    elif ((mark3 > 75) and (mark3 <= 100)):
        grade3 = "Distinction"

    else:
        print("Wrong input")

    if mark4 < 50:
        grade4 = "Fail"

    elif ((mark4 >= 50) and (mark4 <= 65)):
        grade4 = "Pass"

    elif ((mark4 >= 66) and (mark4 <= 75)):
        grade4 = "Credit"

    elif ((mark4 > 75) and (mark4 <= 100)):
        grade4 = "Distinction"

    else:
        print("Wrong input")

    if mark5 < 50:
        grade5 = "Fail"

    elif ((mark5 >= 50) and (mark5 <= 65)):
        grade5 = "Pass"

    elif ((mark5 >= 66) and (mark5 <= 75)):
        grade5 = "Credit"

    elif ((mark5 > 75) and (mark5 <= 100)):
        grade5 = "Distinction"

    else:
        print("Wrong input")

    list1 = [mark1,mark2,mark3,mark4,mark5]
    high_mark = max(list1)
    low_mark = min(list1)

    if high_mark == mark1:
        high_sub = sub1

    elif high_mark == mark2:
        high_sub = sub2

    elif high_mark == mark3:
        high_sub = sub3

    elif high_mark == mark4:
        high_sub = sub4

    elif high_mark == mark5:
        high_sub = sub5

    else:
        print("Wrong Input")

    if low_mark == mark1:
        low_sub = sub1

    elif low_mark == mark2:
        low_sub = sub2

    elif low_mark == mark3:
        low_sub = sub3

    elif low_mark == mark4:
        low_sub = sub4

    elif low_mark == mark5:
        low_sub = sub5

    else:
        print("Wrong Input")

    total = (mark1 + mark2 + mark3 + mark4 + mark5)
    average = total / 5
    if average < 50:
        over_grade = "Fail"

    elif ((average >= 50) and (average <= 65)):
        over_grade = "Pass"

    elif ((average >= 66) and (average <= 75)):
        over_grade = "Credit"

    elif ((average > 75) and (average <= 100)):
        over_grade = "Distinction"

    else:
        print("Wrong input")
    x = round(average,2)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Subject 1:", sub1, "\t", "\t", "Mark:", mark1, "\t", "Grade:", grade1)
    print("Subject 2:", sub2, "\t", "\t", "Mark:", mark2, "\t", "Grade:", grade2)
    print("Subject 3:", sub3, "\t", "\t", "Mark:", mark3, "\t", "Grade:", grade3)
    print("Subject 4:", sub4, "\t", "\t", "Mark:", mark4, "\t", "Grade:", grade4)
    print("Subject 5:", sub5, "\t", "\t", "Mark:", mark5, "\t", "Grade:", grade5)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Highest Marks:", high_mark, "\t", "\t", "Subject:", high_sub)
    print("Lowest Marks:", low_mark, "\t", "\t", "Subject:", low_sub)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Marks:", total)
    print("Average Marks:", x)
    print("Overall Grade:", over_grade)

else:
    print("Wrong input")


