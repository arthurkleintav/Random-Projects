from time import sleep
from random import randint

def write(msg):
    size = len(msg) + 2
    print('~' * size)
    print(f' {msg} ')
    print('~' * size)

def placar():
    print('-=' * 12)
    if player_points > pc_points:
        print(f'\033[32m{f"[ PLAYER: {player_points} ]":>15}')
        print(f'{f"[ COMPUTADOR: {pc_points} ]":>15}\033[m')
    elif pc_points > player_points:
        print(f'\033[31m{f"[ PLAYER: {player_points} ]":>15}')
        print(f'{f"[ COMPUTADOR: {pc_points} ]":>15}\033[m')
    else:
        print(f'\033[36m{f"[ PLAYER: {player_points} ]":>15}')
        print(f'{f"[ COMPUTADOR: {pc_points} ]":>15}\033[m')
    print('-=' * 12)

def menu():
        print('\033[36m--- MENU ---')
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        print('------ ------\033[m')

player_points = 0
pc_points = 0

write('Eu irei jogar Jokenpô com você!')

while True:

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
    print('PÔ!\033[m')
    sleep(0.5)

    print(f'O jogador escolheu {player_choice} e o computador escolheu {pc_choice}.')

    sleep(0.5)

    if winner == 'player':
        print('\033[32mPARABÉNS! O jogador venceu.\033[m')
        player_points += 1
    elif winner == '':
        print('\033[36mEMPATE! Ninguém venceu o jogo.\033[m')
    else:
        print('\033[31mOh não! O jogador perdeu.\033[m')
        pc_points += 1
    
    sleep(0.5)

    placar()

    while True:
        ask = input('Deseja jogar novamente? [S/N]: ').upper().strip()
        if ask in 'SN':
            break
        print('\033[31mERRO! Resposta inválida.\033[m')
    
    if ask == 'S':
        sleep(0.5)
        print('-=' * 12)

    if ask == 'N':
        sleep(0.25)
        write('FINALIZANDO O PROGRAMA... VOLTE SEMPRE!')
        sleep(0.25)
        break
