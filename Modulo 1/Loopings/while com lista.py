def while_com_listas():
    L = []
    while True:
        n=input("Digite uma palavra(0 sai):")
        if n == "pare":
            break
        L.append(n)
    x=0
    while x < len(L):
        print(L[x])
        x=x+1
    print(L)
while_com_listas()