from modelos.livro import Livro

livro4 = Livro('O guia do mochileiro das galáxias', 'Douglas Adams', 2007)
print('Disponivel? ', livro4.disponivel)
livro4.emprestar()
print('Disponivel? ', livro4.disponivel)

print("Livros disponiveis: ", Livro.verificar_disponibilidade(2014))
