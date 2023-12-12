def main():

    divida = float(input("Digite o valor da divida: R$"))
    juros = int(input("Digite o valor dos juros: "))
    valorMensal = float(input("Digite o valor mensal pago: R$"))

    juros = (divida*juros/100)

    totalJuros = 0
    totalPago = 0
    qtdMeses = 0

    while (divida > 0):

        totalJuros = totalJuros + juros
        divida = (divida + juros) - valorMensal
        qtdMeses += 1
        totalPago = totalPago + valorMensal

        
        if (divida + (divida*juros/100)) < valorMensal:
            totalJuros = totalJuros + juros
            divida = (divida + juros)
            totalPago = totalPago + divida
            qtdMeses += 1
            break

    print(f"Total Pago: {totalPago}")
    print(f"Quantidade de meses: {qtdMeses}")
    print(f"Total de Juros: {totalJuros:.2f}")


    #print(f"Total Pago: {totalPago:.2f}\nToral de Juros: {totalJuros:.2f}\nQuantidade de meses: {qtdMeses}")


if __name__=='__main__':
    main()