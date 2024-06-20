# import datetime
# d = datetime.date(2024,5,27)

#outro modo de se fazer:
from datetime import date,datetime,time
#date= ano, mes, dia
#datetime= ano, mes, dia, hora, min, seg

data = date(2024,5,27)
print(data)

print(date.today())

#DATETIME
data_hora = datetime(2024,5,27,10,20,)
print(data_hora)

print(datetime.today())

#TIME
hora = time(13,45)
print(hora)
