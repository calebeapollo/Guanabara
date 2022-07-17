import time, random
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
n2=int(input('Qual sua jogada? ')) #jogada da pessoa

time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!!!')
PEDRA=0
PAPEL=1
TESOURA=2
lista=[PEDRA,PAPEL,TESOURA]
a=random.choice(lista) #escolha do compurador
if a == 0:
    print('Computador jogou PEDRA')
elif a == 1:
    print('Computador jogou PAPEL')
elif a == 2:
    print('Computador jogou TESOURA')
if n2 == 0:
    print('O jogador jogou PEDRA')
elif n2 == 1:
    print('O jogador jogou PAPEL')
else:
    print('O jogaor jogou TESOURA')


