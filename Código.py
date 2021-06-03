def converter():

    print("""
    Conversor e dinheiro:
    [1] Dolar
    [2] Euro
    [3] Yen
    """)

    moeda = int(input('Para qual das moedas você quer converter:'))
    print('-'*42)

    reais = float(input('Quantos reais você quer converter:'))
    print(' ')

    if moeda == 1:
        conver = reais / 5.08
        print('Você converteu R$ {:.2f} para US$ {:.2f}!'.format(reais, conver))

    elif moeda == 2:
        conver = reais / 6.16
        print('Você converteu R$ {:.2f} para € {:.2f}!'.format(reais, conver))

    elif moeda == 3:
        conver = reais / 0.046
        print('Você converteu R$ {:.2f} para ¥ {:.2f}!'.format(reais, conver))

    conver = 0

converter()

teste = True

while teste == True:

    print(' ')
    continuar = str(input('Desejar calcular novamente [Sim] ou [Nao]:'))

    if continuar == 'Sim':
        converter()

    else:
        teste = False

print('Obrigado por usar o conversor!')
