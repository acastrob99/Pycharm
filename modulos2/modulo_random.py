import random

print(random.random()) # Flotante aleatorio >= 0 y < 1.0
print(random.uniform(1,10)) # Flotante aleatorio >= 1 y <10.0
print(random.randrange(10)) # Entero aleatorio de 0 a 9, 10 excluído

help(random)