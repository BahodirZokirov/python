a = int (input ("masala sonini kiriting: "))
if a >= 10 and a <= 40 :
    if a // 10 == 1:
        o = "o'n"
    elif a // 10 == 2:
        o = "yigirma"
    elif a // 10 == 3:
        o = "o'ttiz"
    elif a // 10 == 4:
        o = "qirq"
else:
    o = ""

if a >= 10 and a <= 40 :
    if a % 10 == 0: 
        b = "ta"
    elif a % 10 == 1:
        b = "bitta"
    elif a % 10 == 2:
        b = "ikkita"
    elif a % 10 == 3:
        b = "uchta"
    elif a % 10 == 4:
        b = "to'rtta"
    elif a % 10 == 5:
        b = "beshta"
    elif a % 10 == 6:
        b = "oltita"
    elif a % 10 == 7:
        b = "yettita"
    elif a % 10 == 8:
        b = "sakkizta"
    elif a % 10 == 9:
        b = "to'qqizta"
else:
    b = "xatolik"
print (o, b)
