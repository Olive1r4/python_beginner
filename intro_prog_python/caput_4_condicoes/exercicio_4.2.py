def main():

    velocidade = float(input("Informe a velocidade do caro: "))

    if (velocidade > 80):
        print("Carro foi multado por excesso de velocidade")
        print(f"Valor da multa: R${(velocidade-80)*5}")

if __name__=='__main__':
    main()