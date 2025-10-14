class AnimaisMarinhos:
    def __init__(self, cores, especie, nome, sexo):
        self.cores = cores
        self.especie = especie
        self.nome = nome
        self.sexo = sexo  

    def _artigo(self):
        return 'uma' if self.sexo == 'F' else 'um'

    def dancar(self):
        artigo = self._artigo()
        print(f'Sou {artigo} {self.especie} dançando')

    def cantar(self):
        artigo = self._artigo()
        print(f'Sou {artigo} {self.especie} cantando')

    def nadar(self):
        artigo = self._artigo()
        print(f'Sou {artigo} {self.especie} nadando')

    def viver(self):
        artigo = self._artigo()
        print(f'Sou {artigo} {self.especie} vivendo')

    def brincar(self):
        artigo = self._artigo()
        print(f'Sou {artigo} {self.especie} brincando')


animal1 = AnimaisMarinhos(['azul'], 'peixe', 'Peixinho', 'M')
animal2 = AnimaisMarinhos(['verde'], 'tubarão', 'Martelo', 'M')
animal3 = AnimaisMarinhos(['azul'], 'baleia', 'Baleia', 'F')
animal4 = AnimaisMarinhos(['preto'], 'orca', 'Orca', 'F')
animal5 = AnimaisMarinhos(['rosa'], 'tubarão', 'Tubarão', 'M')
animal1.dancar()
animal2.cantar()
animal3.nadar()
animal4.viver()
animal5.brincar()