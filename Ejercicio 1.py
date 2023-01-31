import datetime
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

start_time = datetime.datetime.now()
fibonacci_recursiva(1)
end_time = datetime.datetime.now()

print("El tiempo de ejercucion es:", end_time - start_time)

start_time = datetime.datetime.now()
fibonacci_bucle(30)
end_time = datetime.datetime.now()

print("El tiempo de ejercucion es:", end_time - start_time)