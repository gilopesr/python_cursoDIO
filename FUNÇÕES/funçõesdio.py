# def exibir_msg():
#      print('olá mundo!')

# def exibir_msg_2(nome):
#     print(f'seja bem vindo {nome}')


# def exibir_3(nome='anonimo'):
#     print(f'seja bem vindo {nome}!')

# exibir_msg()
# exibir_msg_2(nome='giovana')
# exibir_3()
# nome = input('insira seu nome: ')
# exibir_3(nome)

# print(50*'=')

# def calcular_total(numeros):
#     return sum(numeros)

# def retorna_antecessor_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1

#     return antecessor, sucessor

# print(f'{calcular_total([10,20,35])}')
# print(f'{retorna_antecessor_e_sucessor(27)}')

# print(50*'=')

# def salvar_carro(marca,modelo, ano, placa):
#     print(f'carro salvo com sucesso: {marca} / {modelo} / {ano} / {placa}')

# marca = input('insira a marca do seu carro: ')
# modelo = input('insira o modelo do seu carro:')
# ano= input('insira o ano do seu carro: ')
# placa = input('insira a placa do seu carro: ')
# salvar_carro(marca,modelo,ano,placa)

print(50*'=')

def criar_carro(modelo, ano, placa,/, *, marca, motor, combustivel):
    print(modelo,'/', ano,'/', placa,'/', marca,'/', motor,'/', combustivel)
          
criar_carro('range rover', 2023, 'fdf-2020', marca= 'lange rover',motor='2.0', combustivel= 'eletrico')

print(50*'=')

def somar (a,b):
    soma= a+b
    return soma

def exibir_resultado(a,b,funcao):
    resultado=  funcao(a,b)
    print(f'o resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10,27,somar)