def main():

    kmPercorrido = float(input("Digite a quantidade de KM percorrido: "))
    diasAlugados = int(input("Digite a quantidade de dias de Aluguel: "))

    valorPagar = (kmPercorrido*0.15)+(diasAlugados*60)
    print(f"Valor a pagar R$:{valorPagar:5.2f}")

if __name__ == '__main__':
    main()