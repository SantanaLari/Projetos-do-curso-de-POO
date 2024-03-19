from carro import Carro

carro1 = Carro('BMW', '123', 'Preto')
carro2 = Carro('Chevrolet', 'ABC', 'Rosa')
carro3 = Carro('Citroen', 'xyz', 'Cinza')

def main():
    print(f'Carro: {carro1.marca} | Modelo: {carro1.modelo} | Cor: {carro1.cor}')
    print(f'Carro: {carro2.marca} | Modelo: {carro2.modelo} | Cor: {carro2.cor}')
    print(f'Carro: {carro3.marca} | Modelo: {carro3.modelo} | Cor: {carro3.cor}')

if __name__ == '__main__':
    main()