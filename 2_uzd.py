#Izveido programmu, kas ģenerē sarakstu ar n nejaušiem skaitļiem diapazonā 
# no -50 līdz 50. Programma ar for un if palīdzību atrod mazāko un
#  lielāko vērtību sarakstā, 
# bet ar while palīdzību izdrukā visu sarakstu.

import random

n=int(input("Ievadiet skaitļu skaitu: "))
skaitli=[random.randint(-50,50) for _ in range(n)]

print(skaitli)
min_sk=skaitli[0]
max_sk=skaitli[0] # pieņēmumu , kurš ir jāparbauda un jāmaina

for sk in skaitli:
    if sk<min_sk:
        min_sk=sk
    if sk>max_sk:
        max_sk=sk
        print(f"Mazākais skaitlis ir{min_sk}")
        print(f"Lielākais skaitlis ir{max_sk}")

        index=0
        while index<len(skaitli):
            print(f"Skaitlis {index+1}: {skaitli[index]}")
            index+=1

