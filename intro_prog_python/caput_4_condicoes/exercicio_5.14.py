def main():

    qtdNum = 0
    soma = 0

    while True:
        valor = int(input("Digite um números inteiros ou zero para sair:  "))
        if (valor == 0):
            break
        else:
            soma += valor
            qtdNum += 1

    print(f"Quantidade de númeoros digitados: {qtdNum}")
    print(f"Soma dos númeoros digitados: {soma}")
    print(f"Média dos númeoros digitados: {soma/qtdNum}")



if __name__=='__main__':
    main()