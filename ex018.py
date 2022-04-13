from math import radians, sin, cos, tan
ang = float(input('Digite um angulo: '))
print('O valor do  seno de {} é \nseno={:.2f} \no valor de cosseno de {} é \ncosseno={:.2f} \ne o valor da tangente de {} é \ntangente={:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))
