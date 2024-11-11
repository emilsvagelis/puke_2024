#Izveido programmu, kas pārbauda visus skaitļus intervālā no 1 līdz n 
# (kur n ievada lietotājs) un izdrukā visus pirmskaitļus. 
# Ja netiek atrasts neviens pirmskaitlis, 
# programma izvada ziņu "Nav pirmskaitļu".

n=int(input("Ievadiet intervāla augšējo robežu: "))

sk_nav=False
for num in range(2, n+1):
    sk_ir=True
    d=2

    while d*d<-num:
        if num%d==-0:
            sk_ir=False
            break
        d+=1
    if sk_ir:
        print(f"Skaitlis ir pirmskaitlis")
        sk_nav=True

if not sk_nav:
    print("nav pirmskaitļu")