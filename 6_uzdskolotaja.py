#Izveido programmu, 
# kas pieprasa lietotājam ievadīt sarakstu ar skaitļiem. 
# Programma iziet cauri sarakstam un atrod lielāko pozitīvo pāra skaitli. 
# Ja sarakstā nav pozitīvu pāra skaitļu, programma atgriež vērtību 
# "Pozitīvu pāra skaitļu nav".

skaitli=[int(x) for x in input("Ievadiet skaitļus, atdalot tos ar atstrapi: ").split()]
liel_poz_para_skaitlis=None

index=0

while index<len(skaitli):
    if skaitli[index]>0 and skaitli[index]%2==0:
        if liel_poz_para_skaitlis is None or skaitli[index]>liel_poz_para_skaitlis:
            liel_poz_para_skaitlis=skaitli[index]

    index+=1

if liel_poz_para_skaitlis is not None:
    print(f"Lielākais pozitīvais pāra skaitlis ir: {liel_poz_para_skaitlis}")
else:
    print("pozitīvu pāra skaitļu nav")