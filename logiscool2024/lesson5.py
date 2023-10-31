def feladat():
    d=10 #int - egész szám
    b=10.0 #float - tört
    c="10" #str - szöveg
    d=[10] #list - lista
    e=(10, 10) #tuple - olyan lista amin nem lehet változtatni
    print(type(e))


def feladat2():
    a=10.4
    b=3
    c=a/b #tört szám
    c=a//b #egész szám
    print(c)


def feladat3():
    a="alma"
    b="fa"
    print(a, b, sep="")
    print(a, end="")
    print(b)

def feladat4():
    oldalhossz=10
    for i in range(oldalhossz):
        print("o "*(i+1))

def FizzBuzz():
    szam=1