#Exercicio para calcular a raiz quadrada aprximada de um número

def main():
    n = int(input("Digite um numero inteiro: "))
    print(f"A raiz quadrada aproximada do numero {n} é {raiz_quadrada(n):.4}")

#Função para calcular a raiz quadrada aproximada
def raiz_quadrada(num):
    b = 2
    p = (b + num / b) / 2
    while abs(num - p**2) > 0.0001:
        b = p
        p = (b + num / b) / 2
    return p

if __name__=='__main__':
    main()
