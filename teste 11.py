import random
'''PE = float(input('Qual o seu peso '))
AL = float(input('Qual a sua altura '))
IMC = PE / (AL**2)
print ('Seu IMC e: {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Voce esta abaixo do peso. ')
elif 18.5 <= IMC < 25:
    print('Voce esta com o peso normal. ')
elif 25 <= IMC < 30:
    print('Voce esta com sobrepeso.')
else:
    print('Voce esta obeso.')'''

AL = random.randint(1,10)

while True:
    XX = int(input('Digite um numero entre 1 e 10 '))
#while true verifica se uma condicao e verdadeira
    # == equipara um com o outro

    if XX == AL:
        #if = verdadeiro
        print ('Voce acertou')
        break
        #break encerra se a condicao se tornar verdadeira
    else:
        #else = falso
        print('Voce errou, tente novamente ')
