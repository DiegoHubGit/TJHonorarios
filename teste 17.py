No = str(input('Qual o seu nome completo ')).strip()
#strip tras o conteudo completo sem espaco antes e depois das frases
print ('Em maiusculo seu nome e {}.'.format(No.upper()))
print ('Em minusculo seu nome e {}.'.format(No.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(No) - No.count(' ')))
#count ' ' com espaco entre aspas elimina todos os espaco entre os nomes e conta somente os caracteres.
print ('Seu primeiro nome tem {} letras.'.format(No.find(' ')))
#find procura e especifica o conteudo entre ' ', no caso aqui o espaco para sabermos onde acaba o primeiro nome.
#Se = No.split()
#print ('Seu primeiro nome e {}, e ele tem {} letras.'.format(Se[0], len(Se[0])))


