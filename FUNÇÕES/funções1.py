#funções

def entrada():
    num= int(input('digite um numero inteiro e positivo: '))
    while num <= 0:
        num= int(input('digite um numero inteiro e positivo: '))
    return num
    
def qnt_divisor(num):
    conta_divs= 0
    divisor= 1
    while divisor <= num:
        resto = num % divisor
        if resto == 0:
            conta_divs += 1
            divisor += 1
        else:
            divisor += 1
    return conta_divs
    
numero = entrada()
qnt_divisor(numero)
divisores = qnt_divisor(numero)
print(f'{numero} tem {divisores} divisores')
