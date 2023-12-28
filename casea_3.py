a = int (input("Oy tartib raqamini kiriting: "))
if a > 0 and a <= 12:
    if a > 0 and a <= 2 or a == 12:
        result = "Qish"
    elif a >=3  and a <= 5:
        result = "Bahor"
    elif a >=6 and a <= 8:
        result = "Yoz"
    else:
        result = "Kuz"
else:
    result = "Bu songa mos keluvchi fasl topilmadi."
print (result)
