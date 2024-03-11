import random
from math import sqrt, floor
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print ('A raiz de um {} é igual a {:.2f}'.format(num, floor(raiz)))
num = random.randint(1, 100)
print ('Numero da sorte > ',num)




