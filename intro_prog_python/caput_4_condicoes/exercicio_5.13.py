def main():

    divida = float(input("Digite o valor da divida: R$"))
    juros = float(input("Digite o valor dos juros: "))
    valorMensal = float(input("Digite o valor mensal pago: R$"))

    totalPago = 0
    qtdMeses = 0
    totalJuros = 0

    while (divida > 0):
        
        qtdMeses = qtdMeses + 1

        if (divida <= valorMensal):
            totalPago += divida + (divida*juros)
            totalJuros = totalJuros + (divida*juros)
            qtdMeses = qtdMeses + 1
            break
        else:
            continue
    
    print(f"Total Pago: {totalPago:.2f}\nToral de Juros: {totalJuros:.2f}\nQuantidade de meses: {qtdMeses}")


if __name__=='__main__':
    main()