def funcion(n):
    if n%2==0 :
        n=n*5+3
        print n

    else:
        n=n/2+3
        print n

for n in range(50,80):
    funcion(n)
