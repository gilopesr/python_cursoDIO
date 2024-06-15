#classe

class cachorro:
    def __init__(self, nome, cor, acordado = True):
           self.nome = nome
           self.cor = cor
           self.acordado = acordado
                
    def latir(self):
        print('auau')
	
    def dormir(self):
        self.acordado = False
        print('zZzZzZzZ')

# objeto 

cao_1 = cachorro('chopper', 'marrom', False)
cao_2 = cachorro('bambam', 'branco')

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)