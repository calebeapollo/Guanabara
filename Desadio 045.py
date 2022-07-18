from random import randint
import time
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input('Sua jogada: '))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')

print('-'*30)
print(f'Computador jogou {(itens[computador])}')
print(f'Jogador jogou {(itens[jogador])}')
print('-'*30)
if computador == 0:
  if jogador == 0:
   print('Empate')
  elif jogador == 1:
   print('Jogador Ganhou!!')
  else:
      print('Computador Ganhou!!')
elif computador == 1:
     if jogador == 0:
      print('Computador Ganhou!!')
     elif jogador == 1:
         print('Empate!!')
     else:
         print('Jogador Ganhou!!')
elif computador == 2:
    if jogador == 0:
        print('Jogador Ganhou!!')
    elif jogador == 1:
        print('Computador Ganhou!!')
    else:
        print('Empate!!')