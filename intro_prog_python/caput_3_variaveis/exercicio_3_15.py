def main():

    cigarros = int(input("Informe a quantidade de cigarros fomados por dia: "))
    anos = int(input("Informe quantos anos já fumou: "))

    dias = ((((cigarros*(anos*365))*10)/60)/24)

    print(f"Quantidade de tempo de vida perdido: {dias} Dias")
    print(f"Quantidade de tempo de vida perdido: {dias/365:.0f} Anos")

if __name__ == '__main__':
    main()