import datetime
def factorial_recursiva(num):
    num = 1
    if num == 1:
        return 1
    else:
        factorial_recursiva = num - 1 + num + 2
        return factorial_recursiva
def factorial_bucle(num):
   factorial = 1
   for i in range(1, num+1):
       factorial = factorial - 1 + factorial + 2
   return factorial


