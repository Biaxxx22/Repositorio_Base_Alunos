"""
L=[8,7,9,15,19,22,33,44,56,78,90,100,244,332,500]
for Bia in L:
    print(Bia)

L=["lapis","borracha","apontador","cola","estojo",]
for s in L:
    for letra in s:
        print(letra)


L=[1,7,2,4,333,-5,-15,900,500,-25]
maximo=L[0]
for e in L:
    if e > maximo:
        maximo = e
print(maximo)


L=[1,2,3,-8,-90,7,4]
minimo=L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)

for v in range(10):
    print(v)


for v in range(5,8):
    print(v)


for t in range(3,33,3):
    print(t, end=" ")
"""

nome = "Bia"
idade = 15
grana = 25.15
print("%20s tem %010d anos e R$%f no bolso." % (nome,idade,grana))


