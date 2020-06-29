print('*-*-*-*-*-*-*-* CALCULADORA T.M.A. *-*-*-*-*-*-*-*\n'
      'Calculadora de tempo médio de acesso -- versão 1.0\n')

k = ''  # Quantidade de vezes que a palavra foi escrita / variável de início do programa.
while k != 0:
    k = int(input('Entre com o número de vezes que a palavra foi escrita em um curto intervalo de tempo:\n '
                  'Ou tecle "0" para Sair:\n '))
    if k != 0:
        hit = k - 1  # posição acessada está no cache.
        h = hit / k  # Taxa de acertos > fração de todas as referências que puderam ser satisfeitas pelo cache.
        c = 15  # tempo de acesso à cache.
        m = 120  # tempo de acesso à memória principal.
        tma = 15 + (1 - h) * 120

        print(f'\nO tempo médio de acesso é de: {int(tma)}ns!\n')

    else:
        print('Obrigado por usar a CALCULADORA T.M.A.!!')
