def processo_de_conversao_de_dinheiro():
    print("Opções de moedas disponíveis: \n[1] Dolar \n[2] Euro \n[3] Yen")
    print('-' * 42)
    moeda_escolhida = int(input('Para qual das moedas você quer converter:'))
    print('-' * 42)
    quantia_de_reais = float(input('Quantos reais você quer converter:'))
    print(' ')

    if moeda_escolhida == 1:
        valor_final = quantia_de_reais / 5.58
        print('Você converteu R$ {:.2f} para US$ {:.2f}!'.format(quantia_de_reais, valor_final))
    elif moeda_escolhida == 2:
        valor_final = quantia_de_reais / 6.16
        print('Você converteu R$ {:.2f} para € {:.2f}!'.format(quantia_de_reais, valor_final))
    elif moeda_escolhida == 3:
        valor_final = quantia_de_reais / 0.046
        print('Você converteu R$ {:.2f} para ¥ {:.2f}!'.format(quantia_de_reais, valor_final))


processo_de_conversao_de_dinheiro()

repetir_processo = True

while repetir_processo:
    print(' ')
    resposta_calcular_novamente = str(input('Desejar calcular novamente [Sim] ou [Nao]:'))

    if resposta_calcular_novamente == 'Sim':
        processo_de_conversao_de_dinheiro()
    else:
        repetir_processo = False

print('Obrigado por usar o conversor!')
