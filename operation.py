from operations import *
def add(n,m):
    return n+m
def mult(n,m):
    return n*m
def div(n,m):
    return n/m
def soust(n,m):
    return n-m

def fibo(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return  1
    else :
        return fibo(n-1) + fibo(n-2)

fibona = fibo(7)
somme = add(20,50)
print(somme)
print(fibona)
