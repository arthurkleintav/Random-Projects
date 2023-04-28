while True:
    from time import sleep
    from random import randint

    def write(msg):
        size = len(msg) + 4
        print('~' * len(msg))
        print(f' {msg} ')
        print('~' * len(msg))

    write('Eu irei jogar Jokenpô com você!')

    def menu():
        print('\033[36m--- MENU ---')
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        print('------ ------\033[m')

    sleep(1)

    menu()
    lista = ['pedra', 'papel', 'tesoura']

    sleep(0.5)

    while True:
        try:
            player_choice = int(input('Sua escolha: '))
            if player_choice >=1 and player_choice <= 3:
                break
            print('\033[31mERRO! Opção inválida.\033[m')
        except:
            print('\033[31mERRO! Opção inválida.\033[m')

    pc_choice = randint(1, 3)

    if player_choice == 1:
        if pc_choice == 1:
            winner = ''
        elif pc_choice == 2:
            winner = 'pc'
        elif pc_choice == 3:
            winner = 'player'

    elif player_choice == 2:
        if pc_choice == 1:
            winner = 'player'
        elif pc_choice == 2:
            winner = ''
        elif pc_choice == 3:
            winner = 'pc'

    elif player_choice == 3:
        if pc_choice == 1:
            winner = 'pc'
        elif pc_choice == 2:
            winner = 'player'
        elif pc_choice == 3:
            winner = ''

    player_choice = lista[player_choice - 1]
    pc_choice = lista[pc_choice - 1]

    sleep(0.5)
    print('\033[36mJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!\033[m')
    sleep(0.5)

    print(f'O jogador escolheu {player_choice} e o computador escolheu {pc_choice}.')
    sleep(0.5)
    if winner == 'player':
        print('\033[32mPARABÉNS! O jogador venceu.\033[m')
    elif winner == '':
        print('\033[36mEMPATE! Ninguém venceu o jogo.\033[m')
    else:
        print('\033[31mOh não! O jogador perdeu.\033[m')
    
    while True:
        ask = str(input('Deseja jogar novamente? [S/N]: ')).upper().strip()[0]
        if ask in 'SN':
            break
        print('\033[31mERRO! Resposta inválida.\033[m')
    if ask == 'N':
        write('FINALIZANDO O PROGRAMA... VOLTE SEMPRE!')
        sleep(0.25)
        break
