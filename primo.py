n = int(input('informe número a ser testado:\n'))
d1 = n % 2
d2 = n % 3
d3 = n % 5
d4 = n % 7
d5 = n % 11
if d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0 and d5 != 0:
    primo = 1
else:
    primo = 0
if primo == 1:
    print('O número é primo')
else:
    print('O número não é primo')
