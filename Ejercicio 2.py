nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
           "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
           "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
           "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
import csv
dicc = {}
with open('personas.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

def nombrecap(nombre):
    return nombre.tittle()
def numeroDNI(num_nif):
    resto = int(num_nif[0:8]) % 23
    return print(num_nif[0:8] + nif_dict.get(str(resto)))