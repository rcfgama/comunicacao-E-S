print('--------------------------------> Controladores de E/S <-------------------------------\n'
      'Programa para simular o processo geral de comunicação entre CPU e controladoras de E/S.\n'
      '---------------> Assuma o papel da CPU e interaja com as controladoras! <--------------\n')

Disp = ''
while Disp != '1111':
    #  Passo 1: Cpu interroga o dispositivo, enviando o endereço do dispositivo e um sinal dizendo se quer mandar
    #  ou receber dados através da controladora.
    print('Menu Principal "Comunicador E/S":\n '
          'Informe o endereço do dispositivo e se você deseja enviar ou receber dados:\n ')

    Disp = input('0010 > Para receber dados do Dispositivo A.\n'
                 '0011 > Para enviar dados para o Dispositivo A.\n'
                 '0100 > Para receber dados do Dispositivo B.\n'
                 '0101 > Para enviar dados para o Dispositivo B.\n'
                 '1111 > Sair\n ')

    if Disp != '1111':
        while Disp != '0010' and Disp != '0011' and Disp != '0100' and Disp != '0101' and Disp != '1111':
            Disp = input('Endereço não encontrado. Informe um endereço válido, ou "1111" para sair:\n ')

        if Disp != '1111':
            if Disp == '0010':
                Dispname = 'Controladora A'
                data = 'rx'
            elif Disp == '0011':
                Dispname = 'Controladora A'
                data = 'tx'
            elif Disp == '0100':
                Dispname = 'Controladora B'
                data = 'rx'
            else:
                Dispname = 'Controladora B'
                data = 'tx'

            # Passo 2:A controladora, reconhecendo seu endereço, responde quando está pronta para receber (ou enviar)
            # dados.
            if data == 'rx':
                print(Dispname, 'reconheceu seu endereço e está pronta para enviar dados!\n ')

                rxdata = input('Envio dados agora do Dispositivo?\n'
                               '1001 > Envie.\n'
                               '1010 > Aguarde.\n')
                while rxdata != '1001' and rxdata != '1010':
                    rxdata = input('Comando ou instrução inválida. Tente novamente.\n')
                while rxdata == '1010':
                    rxdata = input(Dispname + ' em modo de espera! Entre com "1001" para envio de dados.\n')
                while rxdata != '1001':
                    rxdata = input(Dispname + ' em modo de espera! Entre com "1001" para envio de dados,\n')

            #  Passo 3: A CPU recebe dados através da controladora.
                print('\nDados vindos do Dispositivo:\n '
                      '"Com esse programa, o Ronaldo, aluno gente boa, merece passar.rsrs"\n')

            else:
                print(Dispname, 'reconheceu seu endereço e está pronta para receber dados!\n ')

            #  Passo 3: A CPU envia dados através da controladora.
                txdata = input("Entre com os dados a seguir:\n ")

            # Passo 4: A controlaora responde confirmando que...
                while txdata == '':
                    txdata = input('NAK... not-acknowledge! Aguardando entrada de dados:\n ')

                print('ACK... acknowledge! Informação recebida!\n ')
                show = input('Deseja mostrar agora a saída do programa agora?\n'
                             '1011 > Saída.\n'
                             '1010 > Aguarde.\n')
                while show != '1011' and show != '1010':
                    show = input('Comando ou istrução inválida. Tente novamente:\n ')
                while show == '1010':
                    show = input(Dispname + ' em modo de espera! Entre com "1011" para saída de dados\n')
                while show != '1011':
                    show = input(Dispname + ' em modo de espera! Entre com "1011" para saída de dados\n')
                print('\n' + txdata + '\n')
        else:
            print('Obrigado por usar o Comunicador de E/S!\n')
    else:
        print('Obrigado por usar o Comunicador de E/S!\n')
