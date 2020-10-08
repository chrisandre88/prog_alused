inimesed = int(input("Sisestage inimeste arv: "))
kohad = int(input("Sisestage bussikohtade arv:" ))
bussid = int(input("Sisestage busside arv:" ))

vabadkohad = inimesed - (kohad * bussid)

if vabadkohad < 0:
    vabadkohad = 0
print("Maha jääb " +str(vabadkohad) +" inimest.")