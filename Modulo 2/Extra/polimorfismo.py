'''
este_dicionário = {
    "marca": "chevrolet",
    "modelo":"Opala",
    "ano": 1969
}
print(len(este_dicionário))
'''

from classe_pai import Animal
from classe_pai import AnimaisMarinhos
from classe_pai import Pássaro

animal1 = Animal(2, "Bixo",30, "Unicórnio")
animal2 = AnimaisMarinhos(2,"paracanthurus hepatus",2.5, "Dory")
animal3 = Pássaro(1, "Pintinho", 22, "Piu Piu")

def falar(animal):
    print(f"Tentando falar com {animal.espécie}")
    animal.fazer_som()


print("-"*50)
falar(animal1)

print("-"*50)
falar(animal2)

print("-"*50)
falar(animal3)



