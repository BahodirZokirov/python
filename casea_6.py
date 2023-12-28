'''
1 - detsimetr
2 - kilometr
3 - metr
4 - millimetr
5 - santimetr
'''

kesma = float (input("kesma uzunligini kiriting: "))

a = int (input("uzunlik birligini bildiruvchi son kiriting: 1 - dm, 2 - km, 3 - m, 4 - mm, 5 - sm :"  ))
if a == 1:
    result = f"{kesma * pow (10 , -1 )} metr"
elif a == 2:
    result = f"{kesma * pow (10 , 3 )} metr"
elif a == 3:
    result = f"{kesma * pow (10 , 0 )} metr"
elif a == 4:
    result = f"{kesma * pow (10 , -3 )} metr"
elif a == 5:
    result = f"{kesma * pow (10 , -2 )} metr "
else:
    result = "xato"
print (result)


