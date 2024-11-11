#Izveido programmu, 
# kas pieprasa lietotājam ievadīt paroli līdz 3 mēģinājumiem.
# Ja parole ir nepareiza, programma izvada kļūdas ziņu,
#  bet, ja parole ir pareiza, programma izvada "Laipni lūdzam!".
#  Parolei ir jābūt garākai par 5 rakstzīmēm.

mana_parole="pitris007"


skaititajs=0

while skaititajs<3:
    parole=input("Ievadi paroli: ")
    if len(parole)>5:
        if parole==mana_parole:
            print("Laipni lūdzam vidē!")
            break
        else:
            print("Parole ir nekorekta!")
    else:
        print("Parolei ir jābūt grākai par 5 rakstzīmēm: ")   

    skaititajs+=1

if skaititajs==3:
    print("Pārāk daudz mēģinājumu! ")     

