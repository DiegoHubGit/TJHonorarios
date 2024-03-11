import math
'''co = float(input('Qual a medida do cateto oposto '))
ca = float(input('Qual a medida do cateto adjacente '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A medida da hipotenusa e {.:2f}'.format(hi))
#acima e o primeiro metodo
co = float(input('Qual a medida do cateto oposto '))
ca = float(input('Qual a medidad do cateto adjacente '))
hi = math.hypot(co, ca)
print ('A medida da hipotenusa e {:.2f}'.format(hi))'''
#acima segundo metodo com importacao da hipotenusa
an = float(input('Qual a medida do angulo '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print ('o angulo de {} tem o SENO de {:.2f} \no angulo de {} tem o COSCENO de {:.2f} \no angulo de {} tem a TANGENTE de {:.2f}'.format(an, se, an, co, an, ta))


