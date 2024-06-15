# len ('python')
# len([10,20,30])

class passaro:
    def voar(self):
        print('voando...')

class pardal(passaro):
    def voar(self):
        super().voar()

class avestruz(passaro):
    def voar(self):
        print('avestruz não pode voar')

#exemplo ruim do uso de herança
class aviao(passaro):
    def voar(self):
        print('aviao esta decolando...')

def plano_de_voo(obj):
    obj.voar()

p1 = pardal()
p2 = avestruz()


plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(aviao())
