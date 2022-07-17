n1=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
n2=int(input('Sua opção: '))
if n2 == 1 :
    print(f'Sua compra de R${n1:.2f} vai custar R${n1*0.9:.2f}')
elif n2 <= 2:
    print(f'Sua compra de R${n1:.2f} vai custar R${n1*0.95:.2f}')
elif n2 == 3 :
    print(f'Sua compra será parcelada em 2x de R${n1/2}')
    print(f'Sua compra de R${n1} vai custar R${n1} no final ')
elif n2 <= 4:
    n3 = int(input('Quantas parcelas ? '))
    m = n1 * 0.2 + n1
    print(f'Sua compra será parcelada em {n3}x de R${m / n3:.0f} ')
    print(f'Sua compra de R${n1:.2f} vai custar R${n1 * 1.2:.2f}')
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO.')

print('calebe')

git add . && git commit -m "exercicios" && git push

