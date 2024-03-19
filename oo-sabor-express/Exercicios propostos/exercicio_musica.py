class Musica:
    def __init__(self, nome, artista, duracao):    
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} | Artista: {self.artista} | Duração: {self.duracao}'

musica1 = Musica("Baby, it's okay", "DAY6", 234)
musica2 = Musica("Hurt", "NewJeans", 178)

print(musica1)
