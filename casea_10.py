Y = input ("Yo'nalishni kiriting (Bunda; s-shimol, j-janub, q-sharq, g-g'arb) :")
K = int(input("komandani kiriting (Bunda; 0-to'g'riga, 1-chapga, 2-o'ngga): "))
if (Y == "s" or Y == "j" or Y == "q" or Y == "g") and (K == 0 or K == 1 or K == 2) :
    if Y == "s" and K == 0:
        print ("Shimol, harakatni davom ettir")
    elif Y == "s" and K == 1:
        print ("shimol, chapga buril")
    elif Y == "s" and K == 2:
        print ("shimol, o'ngga buril")
    elif Y == "j" and K == 0:
        print ("janub, harakatni davom ettir")
    elif Y == "j" and K == 1:
        print ("janub, chapga buril")
    elif Y == "j" and K == 2:
        print ("janub, o'ngga buril")
    elif Y == "q" and K == 0:
        print ("Sharq, harakatni davom ettir")
    elif Y == "q" and K == 1:
        print ("sharq, chapga buril")
    elif Y == "q" and K == 2:
        print ("sharq, o'ngga buril")
    elif Y == "g" and K == 0:
        print ("g'arb, harakatni davom ettir")
    elif Y == "g" and K == 1:
        print ("g'arb, chapga buril")
    elif Y == "g" and K == 2:
        print ("g'arb, o'ngga buril")
else:
    print ("xato ma'lumot kiritdingiz!!!")
