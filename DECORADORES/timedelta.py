import datetime

#criando data e hora
d= datetime.datetime(2024,5,14,13,45)
print(d) #2024-05-14 13:45:00

#adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d) #2024-05-21 13:45:00

from datetime import timedelta,datetime

tipo_carro = input('insira o tamanho do carro: "P", "M", "G": ')
tempoP= 30
tempoM = 45
tempoG = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempoP)
    print(f'o carro chegou: {data_atual}\n irá ficar proto em: {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempoM)
    print(f'o carro chegou: {data_atual}\nirá ficar proto em: {data_estimada}')
else: 
    data_estimada = data_atual + timedelta(minutes=tempoG)
    print(f'o carro chegou: {data_atual}\n irá ficar proto em: {data_estimada}')