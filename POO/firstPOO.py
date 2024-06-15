class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    def buzinar(self):
        print('tic tic tic')

    def parar(self):
        print('parando bicicleta....')
        print('bicicleta parada')
    
    def correr(self):
        print('vruuuuuuummm...')

    def trocar_marcha(self):
        print('marcha trocada')
        

b1 = bicicleta('vermelho','caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

#verificar as definições
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2= bicicleta('rosa', 'rodinha', 2023, 899)
print(b2.cor, b2.modelo, b2.ano, b2.valor)
