from datetime import datetime, timezone, timedelta

#criando datetime com timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sp)