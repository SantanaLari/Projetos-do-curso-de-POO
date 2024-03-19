class Livro:

    livro_cadastrado = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livro_cadastrado.append(self)

    def __str__(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Ano: {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano, lista=livro_cadastrado):
       livros = []
       for livro in lista:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros.append(livro.titulo)
       
       return livros
    
livro1 = Livro('E não sobrou nenhum', 'Agatha Christie', 1939)
livro2 = Livro('A escolha', 'Kierra Cass', 2014)

livro3 = Livro('Morte no Nilo', 'Agatha Christie', 1937)
livro3.emprestar()
print('Livro disponivel? ', livro3.disponivel)

Livro.verificar_disponibilidade(1939)
