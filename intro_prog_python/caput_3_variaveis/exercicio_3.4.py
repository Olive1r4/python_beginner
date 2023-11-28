def main():

    salario = float(input("Digite o valor do salário: "))
    print(f"{calcImp(salario)}")

def calcImp(s):
    if (s <= 1200):
        return "Não precisa pagar imposto"
    else:
        return "Precisa pagar imposto"


if __name__ == '__main__':
    main()