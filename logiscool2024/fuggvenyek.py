def tabla_kirajzol(tabla):
    print(tabla[0])
    print(tabla[1])
    print(tabla[2])


def ell(tabla):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == "x":
            return "x nyert"
    for i in range(3):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] == "x":
            return "x nyert"
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == "x":
        return "x nyert"
    if tabla[2][0] == tabla[1][1] == tabla[0][2] == "x":
        return "x nyert"

    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == "o":
            return "o nyert"
    for i in range(3):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] == "o":
            return "o nyert"
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == "o":
        return "o nyert"
    if tabla[2][0] == tabla[1][1] == tabla[0][2] == "o":
        return "o nyert"

    for i in range(3):
        if tabla[0][i] == "-" or tabla[1][i] == "-" or tabla[2][i] == "-":
            return "még tart a játék"
    return "döntetlen"


def lehet_e_ide_rakni(tabla, sor, oszlop):
    if tabla[sor][oszlop] == "-":
        return True
    else:
        return False

def tabla_masol(tabla):
    ujtabla=[]
    for i in tabla:
        ujtabla.append(i)
    return ujtabla


def Max(tabla):
    jelen_szitu = ell(tabla)
    if jelen_szitu == "döntetlen":
        return 0
    elif jelen_szitu == "x nyert":
       return -1
    elif jelen_szitu == "y nyert":
       return 1
    else:
       return 0




def AI(tabla, jelen):
    letezo_lepesek=[]
    for i in range(3):
        for j in range(3):
            if lehet_e_ide_rakni(tabla, i, j):
                letezo_lepesek.append([i,j])
    ertekek=[]
    v=-1000
    for i in letezo_lepesek:
        ujtabla=tabla_masol(tabla)
        ujtabla[letezo_lepesek[0]][letezo_lepesek[1]]=jelen
        e=Max(ujtabla)
        ertekek.append(Max(ujtabla))
        if e>v:
            v=e
    for i in range(len(letezo_lepesek)):
        if ertekek[i]==v:
            return letezo_lepesek[i]

