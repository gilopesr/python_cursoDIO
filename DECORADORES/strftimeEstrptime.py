# import datetime

# d = datetime.datetime.now()

# #formatanmdo data e hora
# print(d.strftime('%d/%m/%Y %H:%M')) #20/05/2024 12:00

# #convertendo string para datetime
# date_string = '27/05/2005 19:45'
# d = datetime.datetime.strptime(date_string, '%d/%m/%Y %H:%M')
# print(d) #2005-05-27 19:45:

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2024-05-20 12:30'
mascara_ptbr = '%d/%m/%Y  %a' #%a = dia da semana
mascara_en = '%Y-%m-%d %H:%M'
print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))