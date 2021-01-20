

print("B & B inn")
print("Breakfast selection")
print("[A]merican Breakfast (RM12.50)")
print("[C]hinese Porridge   (RM 6.30)")
print("[N]asi Lemak         (RM 5.50)")
print("[F]ried Noodle       (RM 5.50)")
print("[L]aksa              (RM 5.30)")
print("[M]ee Mamak          (RM 4.80)")

ipt1 = input("Enter your selection (e.g. A, C):").lower()
ipt2 = int(input("Enter the amount:"))
x = 0
if ipt1 == "a":
    x = float(12.50)

elif ipt1 == "c":
    x = float(6.30)

elif ipt1 == "n":
    x = float(5.50)

elif ipt1 == "f":
    x = float(5.50)

elif ipt1 == "l":
    x = float(5.30)

elif ipt1 == "m":
    x = float(4.80)

else:
    print("Wrong input")

opt = (x * ipt2)

print("Total: RM", opt)


