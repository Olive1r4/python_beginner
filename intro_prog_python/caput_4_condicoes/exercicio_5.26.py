def main():

    num1 = int(input("Informe o primeiro numero inteiro: "))
    num2 = int(input("Informe o segundo numero inteiro: "))

    num3 = 0

    while True:
        if num2 < num1:
            num2 += num2
        else:
            num3 = num1 - num2

if __name__=='__main__':
    main()
