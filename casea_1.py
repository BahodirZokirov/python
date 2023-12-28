a = int (input ("Hafta kuniga mos keluvchi raqamni kiriting: "))
if a > 0 and a <= 7:
    if a == 1:
        day = "Dushanba"
    elif a == 2:
        day = "Seshanba"
    elif a == 3:
        day = "Chorshanba"
    elif a == 4:
        day = "Payshanba"
    elif a == 5:
        day = "Juma"
    elif a == 6:
        day = "Shanba"
    else:
        day = "Yakshanba"
else:
    day = "Bunday songa mos keluvchi hafta kuni topolmadi. "
print (day)
