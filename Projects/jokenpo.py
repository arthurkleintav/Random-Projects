from time import sleep
import random

def write(msg):
    size = len(msg) + 4
    print('~' * len(msg))
    print(f' {msg} ')
    print('~' * len(msg))

write('Eu irei jogar Jokenpô com você!')

def menu():
    print('\033[36m----MENU----')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    print('------ ------\033[m')


