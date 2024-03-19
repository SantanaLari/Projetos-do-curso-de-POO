from carro import Carro
from moto import Moto

carro1 = Carro('Chevrolet', 'Onix', 4)
carro2 = Carro('BMW', 'BMW X5', 4)
carro3 = Carro('Citroen', 'Citroen Jumpy', 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")

def main():
    print('----------- Carros -----------')
    print(carro1)
    print(carro2)
    print(carro3)

    print('----------- Moto -----------')
    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main()