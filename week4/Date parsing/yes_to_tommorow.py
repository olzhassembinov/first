import datetime

x = datetime.datetime.now()
y = datetime.datetime.now()-datetime.timedelta(days=1)
z = datetime.datetime.now()+datetime.timedelta(days=1)

print(f"Yesterday it was {y}, Today is {x} and tommorow {z}")