dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200:
    pp = 0.5 * dist
else:
    pp = 0.45 * dist
print('O valor da passagem para {}km é de {:.2f}'.format(dist, pp))

'''dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200:
    pp = 0.5 * dist
    print('O valor da passagem para {}km é de {:.2f}'.format(dist, pp))
else:
    pp = 0.45 * dist
    print('O valor da passagem para {}km é de {:.2f}'.format(dist, pp))
'''