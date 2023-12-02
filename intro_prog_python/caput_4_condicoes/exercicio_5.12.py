def main():
    # Entrada
    deposito  = float(input("Digite o valor do depósito inicial: "))
    taxa_juros = int(input("Digite o valor da taxa de juros: "))
    depMensal = float(input("Informe o deposito mensal: "))


    # Processamento
    for i in range(24):
        deposito = (deposito+(deposito*(taxa_juros/100)))
        print(f"Valor corrigido ao final do mês {i+1}: {deposito:.2f}")

        deposito = deposito + depMensal


if __name__ == '__main__':
    main()