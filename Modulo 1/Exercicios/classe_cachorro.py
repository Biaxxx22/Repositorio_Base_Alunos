from classe_pai import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super(). __init__(nome)
        self.raca = raca 


    def fazer_som(self):
        print(f"{self.nome} está latindo: Au Au!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo.")

Coragem = Cachorro ('Coragem', 'Beagle')
Coragem.fazer_som()
Coragem.abanar_rabo()

from classe_cachorro import Animal

Dono = Pessoa('Eustácio',70,)





