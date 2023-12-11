def main():

    while True:
        num1 = int(input("Informe o primeiro numero inteiro: "))
        num2 = int(input("Informe o segundo numero inteiro: "))
        if num1 != int:
            print("Você digitou um númro inválido")
            num1 = int(input("Informe o primeiro numero inteiro: "))
        elif num2 != int:
            print("Você digitou um númro inválido")
            num2 = int(input("Informe o primeiro numero inteiro: "))
        else:
            break
                   
if __name__=='__main__':
    main()
