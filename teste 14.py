frase = 'Eu sou Estrategicamente emoldurado'
print (frase[3::3])
print(frase.count('E')) #procurou todos os E Maiusculos
print(frase.upper().count('E')) #transformou todos os E em Maiusculo
print(len(frase))#quantas letras na frase
print(frase.replace('estrategicamente','foda'))#trocou a palavra pela outra
print ('nao' in frase) #proucra a palvra dentro '' na frase
print(frase.find('soul')) #onde comeca o pesquisado dentro ' '
#-1 e resultado para negativo
print(frase.lower().find('estrategicamente'))#joga para minusculo e procura onde comeca a palavra dentro de ' '
print (frase.split()) #cria lista da frase dividap por '  ' !
div = frase.split()
print (div[0]) # dividiu a frase e mostrou somente onde comeca o numero escolhido dentro de ' ' !
print(div[0][1]) # Dividiu mostrou onde inicia a palavra e a letra da palavra escolhida












'''print ("""#frase.len = tamanho frase
#frase.count('o') = quantas letras iguais tem na frase
#frase.count('o,0,13) = quantas letras iguais dentro do intervalo dos numeros descritos
#frase.find('deo') find = encontrar onde comeca o descrito dentro dos '' .
#ferase.find('ALGO INEXISTENTE') = -1 onde nao encontrou nd
#OPERADOR - 'Curso' in frase = TRUE ou FALSE mais nao indica localizacao
#frase.replace('Python','Android') = REPLACE = SUBSTITUIR a '1' pela '2' -
#METODO frase.upper() = Oque for maiusculo mantem , oque nao for ele transforma em MAIUSCULO
#""")

#print com (""") no inicio e fim mostra todas as linhas'''

