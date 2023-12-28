a = int (input ("Karta turini kiriting: 1-g'isht, 2-olma, 3-chillik, 4-qarg'a :"))
b = int (input ("Karta qiymatini kiriting: 11-valet, 12-dama, 13-karol, 14-tuz :"))
if a >= 1 and a <= 4 and b >= 6 and b <= 14:
    if a == 1:
        if b == 6:
            c = "olti g'isht"
        elif b == 7:
            c = "yetti g'isht"
        elif b == 8:
            c = "sakkiz g'isht"
        elif b == 9:
            c = "to'qqiz g'isht"
        elif b == 10:
            c = "o'n g'isht"
        elif b == 11:
            c = "valet g'isht"
        elif b == 12:
            c = "dama g'isht"
        elif b == 13:
            c = "karol g'isht"
        else:
            c = "tuz g'isht"
    elif a == 2:
        if b == 6:
            c = "olti olma"
        elif b == 7:
            c = "yetti olma"
        elif b == 8:
            c = "sakkiz olma"
        elif b == 9:
            c = "to'qqiz olma"
        elif b == 10:
            c = "o'n olma"
        elif b == 11:
            c = "valet olma"
        elif b == 12:
            c = "dama olma"
        elif b == 13:
            c = "karol olma"
        else:
            c = "tuz olma"
    elif a == 3:
        if b == 6:
            c = "olti chillik"
        elif b == 7:
            c = "yetti chillik"
        elif b == 8:
            c = "sakkiz chillik"
        elif b == 9:
            c = "to'qqiz chillik"
        elif b == 10:
            c = "o'n chillik"
        elif b == 11:
            c = "valet chillik"
        elif b == 12:
            c = "dama chillik"
        elif b == 13:
            c = "karol chillik"
        else:
            c = "tuz chillik"
    else:
        if b == 6:
            c = "olti qarg'a"
        elif b == 7:
            c = "yetti qarg'a"
        elif b == 8:
            c = "sakkiz qarg'a"
        elif b == 9:
            c = "to'qqiz qarg'a"
        elif b == 10:
            c = "o'n qarg'a"
        elif b == 11:
            c = "valet qarg'a"
        elif b == 12:
            c = "dama qarg'a"
        elif b == 13:
            c = "karol qarg'a"
        else:
            c = "tuz qarg'a"
else:
    c = "xatolik"
print (c)

        
    
