import random

global szamok
szamok=[]
i=0
while i<50:
    rszam=random.randint(1, 100)
    szamok.append(rszam)
    i+=1

def hettelOszthato():
    print("A lista elemei:")
    i=0
    oszthato=0
    while i<len(szamok):
        if i<len(szamok)-1:
            print(f"\t{szamok[i]}",end=",")
        else:
            print(f"\t{szamok[i]}",end="")
        i+=1
        
    while i<len(szamok):
        if szamok[i]%7==0:
            oszthato+=szamok[i]
        i+=1
    return oszthato

def kiir(szamok, oszthato):
    print(f"{szamok}")
    print(f"\nA listában {oszthato} darab héttel osztható szám van.")

