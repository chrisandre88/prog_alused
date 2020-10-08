vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
ttüüp = int(input("Sisestage treeningu tüüp: "))

meesmax = 220 - vanus
nainemax = round(286- (vanus * 0.88))

if ttüüp == 1:
    mink = 0.50
    maxk = 0.70

if ttüüp == 2:
    mink = 0.70
    maxk = 0.80

if ttüüp == 3:
    mink = 0.80
    maxk = 0.87


if sugu =="N":
    nainemin = round(nainemax * mink)
    nainemax = round(nainemax * maxk)
    print("Pulsisagedus peaks olema vahemikus "+str(nainemin)+" kuni "+str(nainemax)+".")

if sugu =="M":
    meesmin = round(meesmax * mink)
    meesmax = round(meesmax * maxk)
    print("Pulsisagedus peaks olema vahemikus "+str(meesmin)+" kuni "+str(meesmax)+".")

