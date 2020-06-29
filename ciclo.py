print('--------> Bem-Vindo ao Ciclo CPU <--------\n'
      'Simulador de ciclo de instrução de uma CPU\n')
PC = 0
RI = ''
mem = {}

print('Entre com a operação e os endereços. Ao final entre com "1999" para informar fim do ciclo!\n'
      'Obs.1: A memória foi projetada com 8 células conforme o exmplo do trabalho proposto.\n'
      'Obs.2: As operações programadas foram: 1001 = soma, 1010 = subtração, 1011 = multiplicação\n'
      '1100 = divisão, 1110 = incremento, 1111 = módulo\n'
      'Obs.3: O programa foi elaborado para receber as instruções conforme o exemplo do problema:\n'
      '> operação, endereço 1, endereço 2 e o endereço que armazena o resultado.\n')
while RI != '1999':
    mem[PC] = input(f'\nPC diz: "informe instrução "{PC}":\n ')
    RI = mem[PC]
    PC += 1

R0 = mem[0]
RE = {'0': mem[1], '1': mem[2], '2': mem[3]}
print('\nAgora informe os dados!(até 3 campos!)\n')
while PC < 8:
    mem[PC] = input(f'\nPC diz: "informe instrução "{PC}":\n')
    PC += 1

show = input('\nDeseja mostrar saída agora?\n'
             '1. Saída\n'
             '2. Aguarde\n')
while show != '1' and show != '2':
    show = input('Instrução inválida. Tente novamente!')
while show == '2':
    show = input('CPU aguardando instrução para mostrar saída. Tecle "1" para continuar:\n')
while show != '1':
    show = input('CPU aguardando instrução para mostrar saída. Tecle "1" para continuar:\n')
R1 = int(RE['0'])
R2 = int(RE['1'])
RD = {'0': mem[R1], '1': mem[R2]}
R3 = int(RD['0'])
R4 = int(RD['1'])
if R0 == '1001':
    RE['2'] = R3 + R4
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
elif R0 == '1010':
    RE['2'] = R3 - R4
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
elif R0 == '1011':
    RE['2'] = R3 * R4
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
elif R0 == '1100':
    RE['2'] = R3 / R4
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
elif R0 == '1110':
    RE['2'] = R3 + 1
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
else:
    RE['2'] = R3 % R4
    print(f'\nO Resultado no endereço {mem[3]} é {RE["2"]}!\n')
