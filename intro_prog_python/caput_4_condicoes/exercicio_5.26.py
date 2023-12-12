def main():
    numerador = int(input("Informe o numerador: "))
    denominador = int(input("Informe o denominador: "))

    while True:
        if (numerador - denominador) >= 0:
            numerador = numerador - denominador
        else:
            print(f"Resto: {numerador}")
            break


if __name__ == '__main__':
    main()