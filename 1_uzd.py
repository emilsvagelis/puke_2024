#Izveido programmu, kas pieprasa lietotājam ievadīt sarakstu ar skaitļiem.
#  Programma iziet cauri sarakstam un saskaita tikai pozitīvos pāra skaitļus, 
# līdz brīdim, kad sasniedz negatīvu skaitli.
#  Ja sarakstā nav pozitīvu pāra skaitļu, programma atgriež vērtību
#  "Pozitīvu skaitļu nav".

# input... Ievadīt sarakstu ar skaitļiem
# Kas ir saraksts? [4,6,8,5.8,8]
# Kas ir index? 4...0, 6...1, 8...2 --->
skaitli=[int(x) for x in input("Ievadiet skaitļus, atdalot tos ar atstrapi: ").split()]

sum_poz_sk=0
index=0 # mainīgo lietiešu pie while konstrukcijas.

while index<len(skaitli):
    #if skaitli[index]<0:
        #break
    if skaitli[index]>0 and skaitli[index]%2==0:
       sum_poz_sk+=skaitli[index]


    index+=1 # index=index+1

print(f"Summa ir: {sum_poz_sk}")