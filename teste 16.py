'''No = str(input('Qual o seu nome completo ')).strip()

if 'SILVA' in No.upper():
    print ('Seu nome tem Silva! ')
else:
    print('Seu nome nao tem Silva! ')'''

Frase = str(input('Digite uma frase ')).strip().upper()

print ('A letra A aparece {} na sua frase.'.format(Frase.count('A'))) #Aqui deve aparecer quantos A tem a frase inteira
print ('O seu primero A aparece {} na frase!'.format(Frase.find('A')+1)) #aqui deve aparecer onde esta o primeiro A
print ('O seu ultimo A aparece {} na frase!'.format(Frase.rfind('A')+1)) #aqui deve aparecer onde esta o ultimo A'''
