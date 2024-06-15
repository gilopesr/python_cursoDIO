# # #sintaxe da herança
# class A:
#     pass
# class B(A):
#     pass 

# # herança multipla
# class A:
#      pass
# class B(A):
#      pass 
# class C(A,B):
#      pass


class veiculo:
    def __init__(self, cor, placa, numrodas):
        self.cor = cor 
        self.placa = placa
        self.numrodas = numrodas

    def ligar_motor(self):
        print('ligando o motor')

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self,cor, placa, numrodas, carregado):
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'não'} estou carregado")


moto = motocicleta('rosa', 'hello-kitty', 2)
moto.ligar_motor()

carro = carro('azul', 'cinnamon', 4)
carro.ligar_motor()

caminhao = caminhao('roxo', 'kuromi', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
