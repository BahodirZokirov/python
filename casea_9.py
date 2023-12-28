D = int (input("Date ni  kiriting:"))
M = int (input("Month ni  kiriting:"))
if M >= 0 and M <=12 and D >=0 and D <=31:
    
    if M == 1 and D <= 31:
        if D == 31:
            result = "1-fevral"
        else:
            result = f"{D+1}-yanvar"
    elif M == 2 and D <=28:
        if D == 28:
            result = "1-mart"
        else:
            result = f"{D+1}-fevral"
    elif M == 3 and D <=31:
        if D == 31:
            result = "1-aprel"
        else:
            result = f"{D+1}-mart"
    elif M == 4 and D <=30:
        if D == 30:
            result = "1-may"
        else:
            result = f"{D+1}-aprel"
    elif M == 5 and D <= 31:
        if D == 31:
            result = "1-iyun"
        else:
            result = f"{D+1}-may"
    elif M == 6 and D <= 30:
        if D == 30:
            result = "1-iyul"
        else:
            result = f"{D+1}-iyun"
    elif M == 7 and D <= 31:
        if D == 31:
            result = "1-avgust"
        else:
            result = f"{D+1}-iyul"
    elif M == 8 and D <= 31:
        if D == 31:
            result = "1-sentabr"
        else:
            result = f"{D+1}-avgust"
    elif M == 9 and D <= 30:
        if D == 30:
            result = "1-oktabr"
        else:
            result = f"{D+1}-sentabr"
    elif M == 10 and D <= 31:
        if D == 31:
            result = "1-noyabr"
        else:
            result = f"{D+1}-oktabr"
    elif M == 11 and D <= 30:
        if D == 30:
            result = "1-dekabr"
        else:
            result = f"{D+1}-noyabr"
    elif M == 12 and D <= 31:
        if D == 31:
            result = "1-yanvar"
        else:
            result = f"{D+1}-dekabr"
    
else:
    result = "xato"
print (result)
