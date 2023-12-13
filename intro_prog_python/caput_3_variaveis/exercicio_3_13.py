def main():

    temperaturaC = float(input("Digite a temperatura em Celsius: "))
    temperaturaF = ((9*temperaturaC)/5) +32

    print(f"A temperatura convertida de F: {temperaturaF}")

if __name__ == '__main__':
    main()