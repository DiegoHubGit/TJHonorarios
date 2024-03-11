'''N = int(input('Digite um numero '))
#N = str(Nu)
Un = (N // 1 % 10)
De = (N // 10 % 10)
Ce = (N // 100 % 10)
Mi = (N // 1000 % 10)
print ('Analisando o numero {}:'.format(N))
print ('Unidade = {}'.format(Un))
print ('Dezena = {}'.format(De))
print ('Centena = {}'.format(Ce))
print ('Milhar = {}'.format(Mi))'''

Ci = str(input('Digite sua cidade ')).strip()
print (Ci[:5].upper() == 'SANTO')
#assim e o modo correto

# EU fiz isso aqui abaixo
#if 'SANTO' in Ci.upper():
    #print('A cidade comeca com SANTO')
#else:
    #print('A cidade nao comeca com santo')

