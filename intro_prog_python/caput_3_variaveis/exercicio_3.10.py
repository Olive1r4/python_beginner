def main():

    salario = float(input("Digite o valor do Salário: "))
    aumento = float(input("Digite a porcentagem do aumento: "))

    novoSalario = salario + (salario*(1/aumento))

    print(f"Seu novo salário será: {novoSalario}")

if __name__ == '__main__':
    main()
