#desafio 1
def recomendar_plano(consumo):
     if consumo <= 10:
         print('Plano Essencial Fibra - 50Mbps')
     elif consumo >10 and consumo <=20:
         print('Plano Prata Fibra - 100Mbps')
     else:
         print('Plano Premium Fibra - 300Mbps')
     return

consumo = float(input('Insira o seu consumo médio mensal de dados: '))

recomendar_plano(consumo)