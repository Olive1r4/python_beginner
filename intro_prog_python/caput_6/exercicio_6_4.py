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

        if operacao == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ultimo += 1 # Incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S")
if __name__=='__main__':
    main()
