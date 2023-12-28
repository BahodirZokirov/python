a = int (input("og'irlik birligini bildiruvchi son kiriting: 1 - kg, 2 - mg, 3 - gm, 4 - t, 5 - sr :"  ))
o = float (input("Og'irlik qiymatini kiriting: "))


if a == 1:
    result = f"{o * pow (10 , 0 )} kilogramm"
elif a == 2:
    result = f"{o * pow (10 , -6 )} kilogramm"
elif a == 3:
    result = f"{o * pow (10 , -3 )} kilogramm"
elif a == 4:
    result = f"{o * pow (10 , 3 )} kilogramm"
elif a == 5:
    result = f"{o * pow (10 , 2 )} kilogramm "
else:
    result = "xato"
print (result)
