n=int(input("Tabuada de:"))
x=1
while x <= 10:
    print(n,"x",x,"=",x*n)
    x=x+1

def tabuada():
    n=int(input("Digite um numero:"))
    fim=int(input("Digite o final"))
    x=1
    while x <= fim:
        print(n,"x",x,"=",x*n)
        x=x+1


def while_soma():
    s=0
    while True:
        v=int(input("Digite um numero a somar ou 0 para sair:"))
        if v==0:
            break
        s=s+v
    print(s)
