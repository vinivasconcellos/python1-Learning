real = float(input('Quanto você tem na carteira? R$'))
dol = real/6.26
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dol))
