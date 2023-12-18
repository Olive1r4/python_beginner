#Programa 6.7 - Simulação de fila em banco

def main():

    ultimo = 10
    #Cria uma lista de 1 a 10
    fila = list(range(1, ultimo+1))
    while True:
        #Exibe a quantidade de clientes na fila
        print(f"\nExistem {len(fila)} clietes na fila")
        #Exibe a fila
        print(f"Fila atual: {fila}")
        print("Digite F para adicionar um cliente ao final da fila,")
        print("ou A para realizar o atendimeto. S para sair.")
        operacao = input("Operação (F,S ou A): ").upper()

        x = 0
        while True:
            if operacao[x] == "A":
                if len(fila) > 0:
                    atendido = fila.pop(0)
                    print(f"Cliente {atendido} atendido")
                else:
                    print("Fila vazia! Ninguém para atender.")
                x += 1
            elif operacao[x] == "F":
                ultimo += 1 # Incrementa o ticket do novo cliente
                fila.append(ultimo)
                x += 1
            elif operacao[x] == "S":
                exit()
            else:
                print(f"A operação {operacao[x]} é inválida! Digite apenas F, A ou S")
if __name__=='__main__':
    main()
