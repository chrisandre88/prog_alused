pnimi = input("Sisestage Leedu perekonnanimi: ")
if pnimi[-2:] == "ne":
    print("Abielus")
elif pnimi[-2:] == "te":
    print("Vallaline")
elif pnimi[-1] == "e":
    print("Määramata")
else:
    print("Ilmselt ei ole leedulanna perekonnanimi")