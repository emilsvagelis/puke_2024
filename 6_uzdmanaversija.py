#Izveido programmu, 
# kas pieprasa lietotājam ievadīt sarakstu ar skaitļiem. 
# Programma iziet cauri sarakstam un atrod lielāko pozitīvo pāra skaitli. 
# Ja sarakstā nav pozitīvu pāra skaitļu, programma atgriež vērtību 
# "Pozitīvu pāra skaitļu nav".

numbers = [int(x) for x in input("Ievadiet skaitļus, atdalītus ar atstarpi: ").split()]

positive_evens = []

negative_odds = []
 
for num in numbers:
    if num > 0 and num % 2 == 0:
        positive_evens.append(num)
    elif num < 0 and num % 2 != 0:
        negative_odds.append(num)
 
if positive_evens:
    print("Pozitīvo pāra skaitļu summa:", sum(positive_evens))
else:
    print("Nav pozitīvu pāra skaitļu")
if negative_odds:
    print("Negatīvo nepāra skaitļu summa:", sum(negative_odds))
else:
    print("Nav negatīvu nepāra skaitļu")

 