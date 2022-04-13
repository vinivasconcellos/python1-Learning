nome = str(input('Digite seu nome completo: ')).strip().title()
nnome = nome.split()
print('Primeiro = {}'.format(nnome[0]))
print('Último = {}'.format(nnome[len(nnome)-1]))
