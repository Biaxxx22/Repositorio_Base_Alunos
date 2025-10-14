from classe_pai import Animal

class Gato(Animal):

    def miando(self):
        print("Miando...")

    def fazer_som(self):  
        print(f"{self.nome} está miando: Miau!")


gato1 = Gato("Marie")
gato1.fazer_som() 
gato1.miando()    
