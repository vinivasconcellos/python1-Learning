from random import choice
lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
print('O valor escolhido aleatório foi ...')
n = int(input('Digite um número inteiro entre 0 e 5: '))
print('{}.'.format(escolhido))
if n == escolhido:
    print('O usuário venceu!')
else:
    print('O usuário perdeu!')
#outra forma
#from random import randint
#from time import sleep
#computador = randit(0, 5) #Faz o computador "Pensar"
#print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
#jogador = int(input('Em que número pensei? ') #Jogador tenta adivinhar
#print ('PROCESSANDO...')
#sleep(3) #faz dar uma pausa, só pra um suspense
#if jogador == computador:
#   print('PARABÉNS! Você conseguiu me vencer!')
