km = float(input('Quantos km percorridos? '))
d = int(input('Quantos dias de aluguel? '))
pa = 60 * d
pkm = 0.15 * km
pt = pa + pkm
print('O valor total a pagar por {} dias alugados e {:.2f} km percorridos, é de R${:.2f}'.format(d, km, pt))

