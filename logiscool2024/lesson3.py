from fuggvenyek import *
tabla = [
        ['-', '-', '-'],  # 0
        ['-', '-', '-'],  # 1
        ['-', '-', '-']  # 2
]

isRunning = True
sor = 0
oszlop = 0
i = 0
tabla_kirajzol(tabla)
print("Kezdődjék a játék")
while isRunning:
    sor = int(input())
    oszlop = int(input())
    if i % 2 == 0:
        pass
    else:
        tabla[sor][oszlop] = 'o'
    tabla_kirajzol(tabla)
    i += 1
    kilepes = ell(tabla)
    if kilepes == "x nyert":
        print("x nyert")
    elif kilepes == "o nyert":
        print("o nyert")
    else:
        print("még tart a játék")

print("Vége")
