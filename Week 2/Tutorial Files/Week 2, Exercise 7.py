import locale
locale.setlocale(locale.LC_ALL,'')

print("Rainbow stationary")
pen = int(input("Pen:")) #1 pen is RM0.89
pncl = int(input("Pencil:")) #1 pencil is RM0.55
a4_ppr = int(input("A4 paper:")) #1 a4 paper is RM6.79
rlr = int(input("Ruler:")) #1 ruler is RM0.45
total = float((pen*0.89)+(pncl*0.55)+(a4_ppr*6.79)+(rlr*0.45))
print("~**********~")
print(pen,"Pen(s):",locale.currency(pen*0.89))
print(pncl,"Pencil(s):",locale.currency(pncl*0.55))
print(a4_ppr,"Paper(s):",locale.currency(a4_ppr*6.79))
print(rlr,"Ruler(s):",locale.currency(rlr*0.45))
print("Total($) purchase:",locale.currency(total))
print("~**********~")
payment = float(input("Amount Paid:"))
print("Your balance:",locale.currency(payment-total))


      
