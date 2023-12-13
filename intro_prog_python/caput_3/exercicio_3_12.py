def main():

    distancia = float(input("Informe a distânica a percorrer: "))
    velMedia = float(input("Informe a valocidade média: "))

    tempoViagem = (distancia/velMedia)*60
    print(f"Tempo gasto: {tempoViagem} minutos")

if __name__ == '__main__':
    main()