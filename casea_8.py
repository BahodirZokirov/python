D = int (input("Date ni  kiriting:"))
M = int (input("Month ni  kiriting:"))
if M > 0 and M <= 12 and D > 0 and D <= 31:
    if M == 1 and D <= 31:
        result = f"{D}-yanvar"
    elif M == 2 and D <= 28:
        result = f"{D}-fevral"
    elif M == 3 and D <= 31:
        result = f"{D}-mart"
    elif M == 4 and D <= 30:
        result = f"{D}-aprel"
    elif M == 5 and D <= 31:
        result = f"{D}-may"
    elif M == 6 and D <= 30:
        result = f"{D}-iyun"
    elif M == 7 and D <= 31:
        result = f"{D}-iyul"
    elif M == 8 and D <= 31:
        result = f"{D}-avgust"
    elif M == 9 and D <= 30:
        result = f"{D}-sentabr"
    elif M == 10 and D <= 31:
        result = f"{D}-oktabr"
    elif M == 11 and D <= 30:
        result = f"{D}-noyabr"
    elif M == 12 and D <= 31:
        result = f"{D}-dekabr"
    else:
        result = "xato"
else:
    result = "xato"
print(result)
    
