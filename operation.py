#coding:utf-8
def mult(n,m):
   return n*m
def addition(n,m):
    return n+m
def soust(n,m):
    return n-m
def div(n,m):
    return n/m
def fact(n):
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i += 1
    return f
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

if __name__== "__main__":
    fibo=fibonacci(7)
    multi=mult(5,2)
    somme=addition(7,5)
    division=div(8,3)
    soustraction=soust(6,2)
    facto=fact()
    print(division)
    print(soustraction)
    print(somme)
    print(multi)
    print(facto)
    print(fibo)


