#Programa 6.7 - Simulação de fila em banco

def main():

    operacao = []

    ultimo1 = 10
    ultimo2 = 10
    #Cria uma lista de 1 a 10
    fila1 = list(range(1, ultimo1+1))
    fila2 = list(range(1, ultimo2+1))
    while True:
        #Exibe a quantidade de clientes na fila
        print(f"\nExistem {len(fila1)} clietes na fila 1")
        print(f"\nExistem {len(fila2)} clietes na fila 2")
        #Exibe a fila
        print(f"Fila atual: {fila1}")
        print(f"Fila atual: {fila2}")
        print("Digite F para adicionar um cliente ao final da fila,")
        print("A para realizar o atendimeto na fila 1.")
        print("B para realizar o atendimeto na fila 2. S para sair.")
        op = input("Operação (FA, FB, S, A, B): ").upper()

        operacao.append([op])
        print(operacao[0])
        x = 0
        while True:
            if operacao[x] == ["A"]:
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f"Cliente {atendido} atendido")
                else:
                    print("Fila vazia! Ninguém para atender.")
                x += 1
            elif operacao[x] == ["B"]:
                if len(fila2) > 0:
                    atendido = fila2.pop(0)
                    print(f"Cliente {atendido} atendido")
                else:
                    print("Fila vazia! Ninguém para atender.")
                x += 1
            elif operacao[x] == ["FA"]:
                ultimo1 += 1 # Incrementa o ticket do novo cliente
                fila1.append(ultimo1)
                x += 1
            elif operacao[x] == ["FB"]:
                ultimo2 += 1 # Incrementa o ticket do novo cliente
                fila1.append(ultimo2)
                x += 1
            elif operacao[x] == ["S"]:
                exit()
            else:
                print(f"A operação {operacao[x]} é inválida! Digite apenas FA, FB, S, A, B")
if __name__=='__main__':
    main()
