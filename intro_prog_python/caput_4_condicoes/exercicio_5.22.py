def main():

    while True:
        opcao = int(input("Selecione uma das opções do menu:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\nOpção: "))
        
        if (opcao in [1,2,3,4]):

            tabuada = 1

            while tabuada <= 10:
                numero = 1
                while numero <= 10:
                    if (opcao == 1):
                        print(f"{tabuada}+{numero}={tabuada+numero}")
                        numero += 1
                    elif (opcao == 2):
                        print(f"{tabuada}-{numero}={tabuada-numero}")
                        numero += 1
                    elif (opcao == 3):
                        print(f"{tabuada}x{numero}={tabuada*numero}")
                        numero += 1
                    elif (opcao == 4):
                        print(f"{tabuada}÷{numero}={(tabuada/numero):.2f}")
                        numero += 1
                print("------")
                tabuada += 1
        elif (opcao == 5):
            break
        else:
            print("Voce digitou valor incorreto")
            continue

if __name__ == '__main__':
    main()