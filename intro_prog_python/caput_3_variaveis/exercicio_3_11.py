def main():

    valorMercadoria = float(input("Digite o preço da mercadoria: "))
    desconto = float(input("Digite o valor do desconto: "))

    valorDesconto = valorMercadoria*(1/desconto)
    totalPagar = valorMercadoria - valorDesconto

    print(f"Valor do desconto R$: {valorDesconto}")
    print(f"Valor do desconto R$: {totalPagar}")

if __name__ == '__main__':
    main()