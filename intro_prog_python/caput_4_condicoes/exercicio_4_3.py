def main():

    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    if (valor1 > valor2 and valor1 > valor3):
        print(f"O valor {valor1} foi o maior numero digitado")
    elif (valor2 > valor1 and valor2 > valor3):
        print(f"O valor {valor2} foi o maior numero digitado")
    else:
        print(f"O número {valor3} foi o maior numero digitado")

if __name__=='__main__':
    main()