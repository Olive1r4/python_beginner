def main():

    lista1 = []
    lista2 = []
    lista3 = []

    while True:
        n = int(input("Digite numeros inteiros para preencher a lista 1 ou ZERO pra sair: "))
        if n == 0:
            break
        lista1.append(n)

    while True:
        n = int(input("Digite numeros inteiros para preencher a lista 2 ou ZERO pra sair: "))
        if n == 0:
            break
        lista2.append(n)
    lista3.extend([lista1])
    lista3.extend([lista2])
    print(f"Lista 3: {lista3}")
    print(lista3[0])
    print(lista3[0][1])

if __name__ == '__main__':
    main()
