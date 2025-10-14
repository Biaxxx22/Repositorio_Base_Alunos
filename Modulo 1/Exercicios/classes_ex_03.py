class Pessoa:
    def __init__(self, nome, peso, altura):
        self.__nome = nome
        self._peso = peso
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura

    def falar(self):
        return f"{self.__nome} está falando!"





