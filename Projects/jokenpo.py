from time import sleep
import random

def write(msg):
    size = len(msg) + 4
    print('~' * len(msg))
    print(f' {msg} ')
    print('~' * len(msg))

write('Eu irei jogar Jokenpô com você!')
sleep(1)
lista = ['pedra', 'papel', 'tesoura']