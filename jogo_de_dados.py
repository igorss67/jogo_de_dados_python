from random import randint
from time import sleep
from operator import itemgetter
cont = 0
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
hanking = dict()
print('=-' * 20)
for k, v in jogo.items():
    print(f'{k} tirou o valor {v}')
    sleep(0.5)
print('=-' * 20)
hanking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for ind, v  in hanking:
    cont += 1
    print(f'{cont}° lugar: {ind} com {v} pontos')