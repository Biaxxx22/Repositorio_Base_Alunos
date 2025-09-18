itens=[1,2,3,4,5,6,7,8,9,10]
coordenadas=[1.5694,9.3991]
produtos_aleatórios=["espelho","latex","fone","batom","garrafa","teclado","livro","bola","cola","lata"]
print(itens[2])
print(produtos_aleatórios[7])
print(coordenadas[-1])
itens.insert(3,4)
print(itens)
itens.pop(5)
print(itens)

import random

cesta=['maçã','banana','uva','limão']
print(random.choice(cesta))