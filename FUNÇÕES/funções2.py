def exibe_msg():
    print('O fluxograma serve para reealizar conversões de temperatura')
    print('usa-se F->C para calcular fahrenheit para celsius')
    print('usa-se C->F para calcular celsius para fahrenheit')

def get_convert_para():
    resp= input("digite 'F->C' para fahrenheit -> celsius ou digite 'C->F' para celsius -> fahrenheit: ")
    return resp

def exibe_fah_para_celsius(inicio,fim):
    for i in range(inicio,fim+1):
        if inicio <= fim:
            C= (inicio-32) * (5/9)
            print(f'o valor de {inicio} em celsius é {C:.2f}')
            inicio += 1
        else:
            return

def exibe_celsius_para_fah(inicio,fim):
    for i in range(inicio,fim+1):
        if inicio <= fim:
            F= (inicio * (9/5)) + 32
            print(f'o valor de {inicio} fahrenheit é {F:.2f}')
            inicio += 1
        else:
            return

# principal 

exibe_msg()
convert_para = get_convert_para()
if convert_para == 'F->C':
    inicio= int(input('digite a tempratura inicial em fahrenheit: '))
    fim= int(input('digite a tempratura final em fahrenheit: '))
    exibe_fah_para_celsius(inicio,fim)
elif convert_para == 'C->F':
    inicio= int(input('digite a tempratura inicial em celsius: '))
    fim= int(input('digite a tempratura final em celsius: '))
    exibe_celsius_para_fah(inicio,fim)
else: 
    print('digite uma opção valida!')