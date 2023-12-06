def main():

    num = int(input("Digite um número inteiro: "))
    if num in (0,1):
        print(f"O numero: {num} não é um número primo.")
    elif num == 2:
        print(f"O numero: {num} é um número primo.")
    else:
        num_imp: 1
        while num_imp < num:
            if num % 2 == 0:
                while num % num_imp != 0:
                    num_imp += 2

if __name__ == '__main__':
    main()
