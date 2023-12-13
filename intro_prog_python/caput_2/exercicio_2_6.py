def main():

    salario = 750
    aumento = 15

    salario = salario + (salario * (aumento/100))

    print(f"Salário + aumento de {aumento} = {salario}")

if __name__ == '__main__':
    main()