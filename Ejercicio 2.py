import csv
import cProfile

def personas50(archivo):
    file = open(archivo, "r")
    lineas = file.readlines()
    file.close()
    claves = lineas[0][:-1].split(";")
    return print(claves)

archivo = C:\Users\usuario01\Downloads\personas.csv
print(personas50(archivo))
cProfile.run("persona50()")
