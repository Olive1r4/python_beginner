def main():

    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))

    totalSegundos = ((((dias*24)+horas)*60)+minutos)*60

    print(f"Total em segundos: {totalSegundos}")

if __name__ == '__main__':
    main()