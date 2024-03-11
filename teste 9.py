import math
import random
P1 = str(input('Primeiro aluno '))
P2 = str(input('Segundo aluno '))
P3 = str(input('Terceiro aluno '))
P4 = str(input('Quarto aluno '))
lista = [P1, P2, P3, P4]
random.shuffle(lista)
print ('A ordem da apresentacao sera')
print (lista)
#random.shuffle traz a lista criado dentro d e [] embaralhada de forma aleatoria
