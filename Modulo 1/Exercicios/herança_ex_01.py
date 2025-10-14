class Personagens:

    def __init__(self, nome,idade,altura,cor,peso):
        self.nome = nome 
        self.idade = idade
        self.altura = altura
        self.cor = cor
        self.peso = peso


    def comer(self):
        print(f"{self.nome} está comendo.")

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som estranho")       

    def viver(self):
        print(f"{self.nome} está vivendo")





