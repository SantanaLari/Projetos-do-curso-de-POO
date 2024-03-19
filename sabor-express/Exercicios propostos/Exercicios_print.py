# imprima a frase: Python na Escola de Programação da Alura
print('Python na Escola de Programação da Alura')

# Imprima a frase: Meu nome é {nome} e tenho {idade} anos
nome = 'Larissa'
idade = 23

print(f'Meu nome é {nome} e tenho {idade} anos')

# imprima a palavra 'ALURA' de modo que cada letra fique em uma linha
print("""
A
L
U
R
A
""")
# ou
print('A', 'L', 'U', 'R', 'A', sep='\n') 

# imprima a frase: o valor arredondado de pi é: {pi_arredondado}
pi = 3.14159
pi_arredondado = round(pi, 2)
print(f'O valor arredondado de pi é: {pi_arredondado}')