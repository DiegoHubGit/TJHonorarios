import random
import math
'''N = float(input('Qual o numero? '))
print (math.trunc (N))
print ('O valor digitado e {}. E seu numero inteiro e {}'.format(N, int(N)))
#trunc tras o numero inteiro do numero excluindo as casas decimais'''
N1 = str(input('Qual o nome do primeiro canditado ? '))
N2 = str(input('Qual o nome do segundo candidato? '))
N3 = str(input('Qual o nome do terceiro candidato? '))
N4 = str(input('Qual o nome do quarto candidato ? '))
lista = [N1, N2, N3, N4]
sorteado = random.choice(lista)
print ('O sorteado e: {}'.format(sorteado))
#random tem que ser importando - random. choice tu pode escolher um sorteado dentro de uma lsita
#lista se reconhece dentro de []







