class SalaDeAula:
    def __init__(self, numero: int, capacidade: int, nome: str, disciplina: str):
        self.numero = numero
        self.capacidade = capacidade
        self.nome = nome
        self.disciplina = disciplina

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, nome: str, disciplina: str):
        super().__init__(nome)
        self.disciplina = disciplina

    def dar_aula(self, sala: SalaDeAula):
        print(f"O professor {self.nome} de {self.disciplina} esta dando aula na sala {sala.numero}.")


sala = SalaDeAula(152, 7, "Sala", "Fisica")
professor_Will= Professor("Will", "Fisica")
professor_Will.dar_aula(sala)


