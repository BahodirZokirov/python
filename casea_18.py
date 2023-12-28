"""1 dan 999 gach oraliqdagi sonlarni so'zlarda ifodalovchi programma tuzilsin"""
a = int (input("1000 dan kichik musbat son kiriting:"))
t = a % 100
if a >= 1 and a <= 999:
    if a // 100 == 1:
        y = "bir yuz"
    elif a // 100 == 2:
        y = "ikki yuz"
    elif a // 100 == 3:
        y = "uch yuz"
    elif a // 100 == 4:
        y = "to'rt yuz"
    elif a // 100 == 5:
        y = "besh yuz"
    elif a // 100 == 6:
        y = "olti yuz"
    elif a // 100 == 7:
        y = "yetti yuz"
    elif a // 100 == 8:
        y = "sakkiz yuz"
    elif a // 100 == 9:
        y = "to'qqiz yuz"
    else:
        y = ""
    if t // 10 == 1:
        o = "o'n"
    elif t // 10 == 2:
        o = "yigirma"
    elif t // 10 == 3:
        o = "o'ttiz"
    elif t // 10 == 4:
        o = "qirq"
    elif t // 10 == 5:
        o = "ellik"
    elif t // 10 == 6:
        o = "oltmish"
    elif t // 10 == 7:
        o = "yetmish"
    elif t // 10 == 8:
        o = "sakson"
    elif t // 10 == 9:
        o = "to'qson"
    else:
        o = ""
    if a % 10 == 1:
        b = "bir"
    elif a % 10 == 2:
        b = "ikki"
    elif a % 10 == 3:
        b = "uch"
    elif a % 10 == 4:
        b = "to'rt"
    elif a % 10 == 5:
        b = "besh"
    elif a % 10 == 6:
        b = "olti"
    elif a % 10 == 7:
        b = "yetti"
    elif a % 10 == 8:
        b = "sakkiz"
    elif a % 10 == 9:
        b = "to'qqiz"
    else:
        b = ""
    
else :
    y = "xato son kiritdingiz!!!!!!"
    if y == "xato son kiritdingiz!!!!!!":
        b = ""
        o = ""
print (y, o, b)
