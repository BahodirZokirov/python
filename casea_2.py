a = int (input ("Bahoni kiriting: "))
if a > 0 and a <= 5:
    if a == 1:
        result = "yomon"
    elif a == 2:
        result = "qoniqarsiz"
    elif a == 3:
        result = "qoniqarli"
    elif a == 4:
        result = "yaxshi"
    else:
        result = "a'lo"
else:
    result = "xato"
print(result)
