a = input("Lokatr qarab turgan tomonni kiriting (Bunda; s-shimol, j-janub, q-sharq, g-g'arb) :")
b = int (input("komandani kiriting ,(Bunda; 0-o'ngga buril, 1-chapga buril, 2-180 gradus aylan) :"))
if (a == "s" or a == "j" or a == "q" or a == "g") and (b == 0 or b == 1 or b == 2):
    if a == "s" and b == 0:
        c = "Sharq"
    elif a == "s" and b == 1:
        c = "G'arb"
    elif a == "s" and b == 2:
        c = "Janub"
    elif a == "j" and b == 0:
        c = "G'arb"
    elif a == "j" and b == 1:
        c = "Sharq"
    elif a == "j" and b == 2:
        c = "Shimol"
    elif a == "q" and b == 0:
        c = "Janub"
    elif a == "q" and b == 1:
        c = "shimol"
    elif a == "q" and b == 2:
        c = "G'arb"
    elif a == "g" and b == 0:
        c = "Shimol"
    elif a == "g" and b == 1:
        c = "Janub"
    else:
        c = "Sharq"
else:
    c = "xatolik"
print (c)
