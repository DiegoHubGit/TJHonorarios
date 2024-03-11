T = float(input('Informe a temperatura em ºC: '))
F = ((9*T)/5+32)
print('A temperatura de {}ºC corresponde a {} ºF'.format(T, F))
D = float(input('Quantos dias alugados? '))
KM = float(input('Quantos KM rodados? '))
Dia = float(input('Qual o valor da diaria? '))
KMR = float(input('Qual o valor do KM rodado? '))
print('O total a pagar é de R${:.2f}'.format((D*Dia)+(KM*KMR)))

