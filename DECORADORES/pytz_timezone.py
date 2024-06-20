import pytz_timezone
from datetime import datetime
data = datetime.now(pytz_timezone.timezone('Europe/Oslo'))
data2 = datetime.now(pytz_timezone.timezone('America/Sao_Paulo'))

print(data)