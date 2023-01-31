import cProfile
def fibonacci_recursiva(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2)


def fibonacci_bucle(n):
    a = 0
    b = 1
    for k in range(n):
        c = b + a
        a = b
        b = c
    return a

cProfile.run("fibonacci_recursiva(3)")


