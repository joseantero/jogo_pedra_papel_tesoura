import random
from time import sleep
print('**********Jogo Jankenpô************')
sleep(1)
sorteado = random.choice(['pedra','papel','tesoura'])
jogador = str(input('Chegou a sua vez....\n Pedra;\n Papel;\nTesoura;\ndigite a sua escolha:'))
print(f'a minha escolha é {sorteado}\n logo......')
if jogador == sorteado:
    print(f'\033[1:33m EMPATE - Eu escolhi {sorteado} e você também {jogador}')
elif jogador == 'pedra' and sorteado == 'papel':
    print(f'\033[1:31m VOCÊ PERDEU, eu escolhi o {sorteado} que embrula e vence á {jogador}')
elif jogador == 'tesoura' and sorteado == 'papel':
    print(f'\033[1:32m VOCÊ ME VENCEU,eu escolhi o {sorteado} que é cortado pela {jogador}')
elif jogador == 'pedra' and sorteado == 'tesoura':
    print(f'\033[1:32m VOCÊ ME VENCEU,eu escolhi a {sorteado} que é quebrada pela {jogador}')
elif jogador == 'tesoura' and sorteado == 'pedra':
    print(f'\033[1:31m VOCÊ PERDEU, a minha escolha {sorteado} quebra a sua {jogador}')
elif jogador == 'papel' and sorteado == 'pedra':
    print(f'\033[1:32m VOCÊ ME VENCEU, a sua escolha {jogador} embrula e vence á minha escolha:{sorteado}')
elif jogador == 'papel' and sorteado == 'tesoura':
    print(f'\033[1:31m VOCÊ PERDEU, o {jogador} é cortado pela minha escolha: {sorteado}')
