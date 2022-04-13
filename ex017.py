from math import sqrt
c1 = float(input('Digite cateto 1: '))
c2 = float(input('Digite cateto 2: '))
hp = (c1**2)+(c2**2)
h = sqrt(hp)
print('O triângulo, de cateto {} \ne cateto {}, \ntem uma hipotenusa de {:.2f}'.format(c1, c2, h))
#dá pra usar a função hypot, que é hipotenusa dentro do math