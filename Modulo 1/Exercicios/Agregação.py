class Mídia:
    def __init__ (self, título:str, artista:str):
        self.titulo = título
        self.artista = artista

class Musica(Mídia):
    def __repr__(self):
        return f" ' {self.titulo}' por {self.artista}"
    
class Playlist:
    def __init__(self, nome:str, musicas: list[Musica]):
        self.nome = nome
        self.musicas = musicas

    def tocar_todas(self):
        print(f"\n Tocando a playlist '{self.nome}':")
        for musica in self.musicas:
            print(f"  Tocando agora: {musica}")
        

musica_1 = Musica("Young and beautiful","Lana del Rey")
musica_2 = Musica("Miserable Man","David Kushner")
musica_3 = Musica("Dead mean","David Kushner")

daylist = Playlist("Sua playlist diária",
                    [musica_1, musica_2, musica_3])

daylist.tocar_todas()
