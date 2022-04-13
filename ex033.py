n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))
n3 = int(input('Digite N3: '))
if n1 > n2 and n1 > n3:
    print('N1 {} é o maior.'.format(n1))
if n2 > n1 and n2 > n3:
    print('N2 {} é o maior.'.format(n2))
if n3 > n1 and n3 > n2:
    print('N3 {} é o maior.'.format(n3))
if n1 < n2 and n1 < n3:
    print('N1 {} é o menor.'.format(n1))
if n2 < n1 and n2 < n3:
    print('N2 {} é o menor.'.format(n2))
if n3 < n1 and n3 < n2:
    print('N3 {} é o menor.'.format(n3))
