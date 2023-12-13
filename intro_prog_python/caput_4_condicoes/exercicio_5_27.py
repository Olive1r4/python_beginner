# Verifia se o número é palindromo

def main():

    numero = int(input("Digite um número inteiro: "))
    palindromo = 0
    num = numero

    while num != 0:
        ultimo_numero = num % 10
        palindromo = palindromo*10 + ultimo_numero
        num = int(num / 10)
    if palindromo == numero:
        print(f"O {numero} é um Palíndromo")
    else:
        print(f"O {numero} não é um Palíndromo")

if __name__ == '__main__':
    main()
