A = float ( input ("Birinchi sonni kiriting:"))
B = float ( input ("Ikkinchi sonni kiriting:"))
C = int (input ("Amal sonini kiriting: "))
if C > 0 and C <= 4:
    if C == 1:
        result = A + B
    elif C == 2:
        result = A - B
    elif C == 3:
        result = A / B
    else:
        result = A * B
else:
    result = "Bunday amal soni topilmadi."
print ("Natija: ", result)
