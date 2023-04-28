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

sleep(0.5)

menu()
lista = ['pedra', 'papel', 'tesoura']

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

player_choice = lista[player_choice - 1]
pc_choice = lista[pc_choice - 1]

print(f'O jogador escolheu {player_choice} e o computador escolheu {pc_choice}.')
if winner == 'player':
    print('\033[32mPARABÉNS! O jogador venceu.\033[m')
elif winner == '':
    print('\033[36mEMPATE! Ninguém venceu o jogo.\033[m')
else:
    print('\033[31mOh não! O jogador perdeu.\033[m')
