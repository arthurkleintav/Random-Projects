from time import sleep
import random

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

while True:
    try:
        choice = int(input('Sua escolha: '))
        if choice >=1 and choice <= 3:
            break
        print('\033[31mERRO! Opção inválida.\033[m')
    except:
        print('\033[31mERRO! Opção inválida.\033[m')
