a = int (input("Teng yonli uchnurchak elementlarini kiriting: (Bunda: 1-katet, 2- gipotenuza, 3-balandlik, 4-yuza)"))
b = float (input ("Miqdorni kiriting: "))
if a == 1 or a == 2 or a == 3 or a ==4:
    if a == 1:
        c = f"Katet = {b}, gipotenuza = {b * pow(2, 1/2)}, balandlik = {(b * 2 ** (1/2)) / 2}, yuza =  {b * b / 2}"
    elif a == 2:
        c = f" Katet = {b / pow(2, 1/2)}, gipotenuza = {b}, balandlik = {(b / 2)}, yuza =  {b * b / 4}"
    elif a == 3:
        c = f" Katet = {2 * b / pow(2, 1/2)}, gipotenuza = {2 * b}, balandlik = {b}, yuza =  {b ** 2}"
    elif a == 4:
        c = f" Katet = {(2 * b ** (1/2) ) / 2 ** (1/2)}, gipotenuza = {2 * b ** (1/2)}, balandlik = {b ** (1/2)}, yuza =  {b}"
else :
    c = "xatolik"

print(c)
