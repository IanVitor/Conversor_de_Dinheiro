import random
num = (random.randint(1, 9))
print('''Vamos brincar de adivinhar!
Digite um valor e tente a sorte para acertar''')
acerto = int(input('Digite um valor:'))
while acerto != num:
    if acerto < num:
        print('Quase! Digite um valor maior!')
    elif acerto > num:
        print('perto! Digite um valor menor!')
    acerto = int(input('Digite um valor:'))
print('''Parabéns, você acertou! 
O número sorteado foi o {}!'''.format(num))
