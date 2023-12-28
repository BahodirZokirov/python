import math
a = int (input ("Doira elementlarini kiriting: (1-radius, 2- diametr, 3-doira uzunligi, 4-doira yuzasi) "))
b = float (input ("kattalikni kiriting: "))
if a == 1:
    result = f"R = {b}, D = {2*b}, L = {math.pi*2*b}, S = {math.pi * pow(b, 2)} "
elif a == 2:
    result = f"R = {b/2}, D = {b}, L = {math.pi*b}, S = {math.pi * pow(b/2, 2)} "
elif a == 3:
    result = f"R = {b / ( 2 * math.pi )}, D = {b / math.pi}, L = {b}, S = {math.pi * pow(b / (2 * math.pi) , 2)} "
elif a == 4:
    result = f"R = {math.sqrt (b / math.pi)}, D = {2 * math.sqrt (b / math.pi)}, L = {math.pi * 2 * math.sqrt (b / math.pi)}, S = {b}"
print (result)
