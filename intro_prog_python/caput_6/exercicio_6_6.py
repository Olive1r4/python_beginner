def main():

    operacao = []

    ultimo1 = 10
    ultimo2 = 10
    # Cria uma lista de 1 a 10
    fila1 = list(range(1, ultimo1+1))
    fila2 = list(range(1, ultimo2+1))
    while True:
        # Exibe a quantidade de clientes na fila
        print(f"\nExistem {len(fila1)} clientes na fila 1")
        print(f"\nExistem {len(fila2)} clientes na fila 2")
        # Exibe a fila
        print(f"Fila atual 1: {fila1}")
        print(f"Fila atual 2: {fila2}")
        print("Digite F para adicionar um cliente ao final da fila,")
        print("A para realizar o atendimento na fila 1.")
        print("B para realizar o atendimento na fila 2. S para sair.")
        op = input("Operação (FA, FB, S, A, B): ").upper()

        operacao.append(op)
        x = 0
        while x < len(operacao):
            if operacao[x] == "A":
                if len(fila1) > 0:
                    atendido = fila1.pop(0)
                    print(f"Cliente {atendido} atendido na fila 1")
                else:
                    print("Fila 1 vazia! Ninguém para atender.")
                x += 1
            elif operacao[x] == "B":
                if len(fila2) > 0:
                    atendido = fila2.pop(0)
                    print(f"Cliente {atendido} atendido na fila 2")
                else:
                    print("Fila 2 vazia! Ninguém para atender.")
                x += 1
            elif operacao[x] == "FA":
                ultimo1 += 1  # Incrementa o ticket do novo cliente
                fila1.append(ultimo1)
                x += 1
            elif operacao[x] == "FB":
                ultimo2 += 1  # Incrementa o ticket do novo cliente
                fila2.append(ultimo2)
                x += 1
            elif operacao[x] == "S":
                exit()
            else:
                print(f"A operação {operacao[x]} é inválida! Digite apenas FA, FB, S, A, B")
                x += 1


if __name__ == '__main__':
    main()
