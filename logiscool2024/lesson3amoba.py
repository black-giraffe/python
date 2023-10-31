from lesson3 import *
i = 0
tabla_kirajzol(tabla)
while isRunning:
    sor = int(input())
    oszlop = int(input())
    if i % 2==0:
        tabla[sor][oszlop]="x"
    else:
        tabla[sor][oszlop] = "0"
    tabla_kirajzol(tabla)
    i+=1
    kilepes=ell(tabla)
    if kilepes =="x nyert":
        print("x nyert")
    elif kilepes == "o nyert":
        print("o nyert")
    else:
    print("még tart a játék")

print("Vége")
