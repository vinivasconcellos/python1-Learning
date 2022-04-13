nome = str(input('Qual o seu nome? ')).strip().title()
if nome == 'Vinícius':
    print('Que nome lindo você tem!')
else:
    print('Gostei do seu nome.')
print('Bom dia {}'.format(nome))
