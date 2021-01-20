def main_menu():
    print("""\n[1]Ingredients Purchase
[2]DIY Soap Courses
[3]Calculate and Quit
""")
    first_ipt = input("Choice:")

    return first_ipt

def ingredients():
    print("The DIY Soap Shop")

    olive = float(input("Olive Oil (ounces):"))
    coconut = float(input("Coconut Oil (ounces):"))
    palm = float(input("Palm Oil (ounces):"))
    shea = float(input("Shea Butter (ounces):"))
    lye = float(input("Lye (ounces):"))

    return olive, coconut, palm, shea, lye

def courses():
    print("DIY Soap Courses")
    print("""[4]days DIY Soap Courses
[5]days DIY Soap Courses
[6]days DIY Soap Courses
""")

    choice = input("Choice:")

    return choice
