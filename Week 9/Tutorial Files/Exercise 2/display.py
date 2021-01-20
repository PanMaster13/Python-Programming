def display():
    name = input("Customer name:")
    file = open("Purchase Record.txt", "w")
    file.write("""
Customer Name: {}
A4 paper (canon): {} ~ RM: {}
A4 paper (rainbow): {} ~ RM: {}
Long ruler: {} ~ RM: {}
Short ruler: {} ~ RM: {}
Blue Pen: {} ~ RM: {}
Red Pen: {} ~ RM: {}
Black Pen: {} ~ RM: {}
2B Pencil: {} ~ RM: {}
Total: {}
""".format(str(name), str(quantity1), str(price1), str(quantity2), str(price2), str(quantity3), str(price3), str(quantity4), str(price4), str(quantity5), str(price5), str(quantity6),str(price6),str(quantity7),str(price7),str(quantity8), str(price8),  str(total)))
