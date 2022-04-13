sal = float(input('Qual o salário do funcionário? '))
if sal <= 1250:
    nsal = sal * 1.15
else:
    nsal = sal * 1.10
print('O novo salário do funcionário vai ser: R${:.2f}'.format(nsal))
