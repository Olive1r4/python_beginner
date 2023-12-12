def main():
    num = int(input("Digite um número inteiro: "))
    if num in (0,1):
        print(f"O numero {num} não é primo.")
    elif num == 2:
        print(f"O numero {num} é primo.")
    else:
        num_imp = 3
        while num_imp < num:
            if num % 2 == 0:
                print(f"O número {num} não é primo")
                break
            if num % num_imp == 0:
                print(f"O número {num} não é primo")
                break
            num_imp += 2
        print(f"O número {num} é primo")
if __name__ == '__main__':
    main()
