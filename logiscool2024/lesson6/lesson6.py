lista1 = [0, 1, 2, 3]
lista2 = lista1 #ikrek lesznek
lista1.append(7)
print(lista2)
lista3 = lista1[:] #nem lesznek ikrek

szotar={"cat":"cica", "dog":"kutya"}
szotar["apple"]="alma"
#szotar.update({"car":"autó", 2:"kettő"})



for i in szotar.keys():
    print(i)

print(szotar.values())

def feladat3():


    print("kinyitjuk a fájlt")
    f=open("file.txt", "w")
    f.write("hello file")
    print("bezárjuk a fájlt")
    f.close()    
feladat3()