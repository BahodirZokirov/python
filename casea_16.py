a = int (input ("Yoshni kiriting:"))
if a // 10 >= 0 and a // 10 <= 10 and a < 110:
    if a // 10 == 0:
        o = ""
    elif a // 10 == 1:
        o = "o'n"
    elif a // 10 == 2:
        o = "yigirma"
    elif a // 10 == 3:
        o = "o'ttiz"
    elif a // 10 == 4:
        o = "qirq"
    elif a // 10 == 5:
        o = "ellik"
    elif a // 10 == 6:
        o = "oltmish"
    elif a // 10 == 7:
        o = "yetmish"
    elif a // 10 == 8:
        o = "sakson"
    elif a // 10 == 9:
        o = "to'qson"
    elif a // 10 == 10:
        o = "bir yuz"
else:
    o = ""



if a % 10 >= 0 and a % 10 <=9 and a < 110 and a // 10 >= 0 and a // 10 <= 10:
    if a % 10 == 0:
        b = ""
    elif  a % 10 == 1:
        b = "bir"
    elif  a % 10 == 2:
        b = "ikki"
    elif  a % 10 == 3:
        b = "uch"
    elif  a % 10 == 4:
        b = "to'rt"
    elif  a % 10 == 5:
        b = "besh"
    elif  a % 10 == 6:
        b = "olti"
    elif  a % 10 == 7:
        b = "yetti"
    elif  a % 10 == 8:
        b = "sakkiz"
    elif  a % 10 == 9:
        b = "to'qqiz"
else:
    b = "Xato!!!!!"



if a // 10 == 0 and a % 10 == 0:
    b = "nol"
print(o, b)




    
