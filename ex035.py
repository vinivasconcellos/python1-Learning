n1 = int(input('Digite a reta1: '))
n2 = int(input('Digite a reta2: '))
n3 = int(input('Digite a reta3: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possível formar um triângulo com {}, {} e {}.'.format(n1, n2, n3))
else:
    print('Não é possível formar um triângulo com {}, {} e {}.'.format(n1, n2, n3))
