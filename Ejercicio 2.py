import csv
import cProfile
nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
           "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
           "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
           "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}

def check_username(nombre):
    return nombre.tittle()
def check_nif(num_nif):
    resto = int(num_nif[0:8]) % 23
    return print(num_nif[0:8] + nif_dict.get(str(resto)))

def check_file(fichero_50, fichero_1000):
    lista = []
    with open("fichero_50", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', dialect=csv.excel)
        for gente in reader:
            lista.append(gente)

    with open("fichero_1000", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', dialect=csv.excel)
        for gente in reader:
            lista.append(gente)

    for persona in lista:
        persona[0] = check_username(usuario[0])
        persona[1] = check_username(usuario[1])

    with open("fichero_50", encoding="utf-8") as csvfile:
        csvresult = open("fichero_final.csv", "w", newline="")
        final =csv.writer(csvresult, quatechar=" ", quoting=csv.quote_all)
        for linea in lista:
            final.weiterow(linea)


cProfile.run("leer_ficheros('50.csv', '1000.csv')")