def main():

    lista1 = []
    lista2 = []
    lista3 = []

    while True:
        num = int(input('Digite um número inteiro para a lista 1 ou ZERO para sair: '))
        if num == 0:
            break
        lista1.append(num)
    while True:
        num = int(input('Digite um número inteiro para a lista 2 ou ZERO para sair: '))
        if num == 0:
            break
        lista2.append(num)
    x = 0
    while x < len(lista1) :
        if lista1[x] not in lista3:
            lista3.append(lista1[x])
            x += 1
        else:
            x += 1
    x = 0
    while x < len(lista2) :
        if lista2[x] not in lista3:
            lista3.append(lista2[x])
            x += 1
        else:
            x += 1
    print(f"Lista 3: {lista3}")
if __name__=='__main__':
    main()
