def main():
    # Entrada
    deposito  = int(input("Digite o valor do depósito inicial: "))
    taxa_juros = int(input("Digite o valor da taxa de juros: "))

    # Processamento
    for i in range(24):
        deposito = deposito+(deposito*(taxa_juros/100))
        print(f"Valor corrigido no mês {i+1}: {deposito:.2f}")
    
if __name__ == '__main__':
    main()