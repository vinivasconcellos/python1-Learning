vel = float(input('Qual a velocidade? '))
if vel > 80:
    print('Você foi multado!. Sua velocidade foi de {} km/h.'.format(vel))
    di = vel - 80
    multa = 7 * di
    print('Sua multa será no valor de R$ {:.2f}.'.format(multa))
else:
    print('Dirija com segurança. Não ultrapasse 80km/h!')
