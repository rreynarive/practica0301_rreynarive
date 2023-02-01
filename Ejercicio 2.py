import cProfile
import csv
def personas50():
    with open("50.csv", r) as file:
        print(file.read())


def fibonacci_bucle(n):
    a = 0
    b = 1
    for k in range(n):
        c = b + a
        a = b
        b = c
    return a

cProfile.run("fibonacci_recursiva(3)")


