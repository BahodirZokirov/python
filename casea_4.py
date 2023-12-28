a = int (input("Oy tartib raqamini kiriting: "))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    result = "Bu oyda 31 kun bor"
elif a == 4 or a == 6 or a == 9 or a == 11:
    result = "Bu oyda 30 kun bor"
elif a == 2:
    result = "Bu oyda 28 kun bor"
else:
    result = "Bu songa mos keluvchi oy topilmadi."
print (result)
