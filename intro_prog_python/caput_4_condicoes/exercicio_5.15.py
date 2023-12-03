def main():

    totalCompras = 0

    while True:
        prodCod = int(input("Digite o código do produto ou zero para sair: "))
        if (prodCod == 1):
            qtdProd = float(input("Digite a quantidade de produtos: "))
            totalCompras += qtdProd*0.50
        elif (prodCod == 2):
            qtdProd = int(input("Digite a quantidade de produtos: "))
            totalCompras += qtdProd*1.00
        elif (prodCod == 3):
            qtdProd = int(input("Digite a quantidade de produtos: "))
            totalCompras += qtdProd*4.00
        elif (prodCod == 5):
            qtdProd = int(input("Digite a quantidade de produtos: "))
            totalCompras += qtdProd*7.00
        elif (prodCod == 9):
            qtdProd = int(input("Digite a quantidade de produtos: "))
            totalCompras += qtdProd*8.00
        elif (prodCod == 0):
            print(f"Total de compras: R$ {totalCompras}")
            break
        else:
            print("Código inválido")

if __name__ == '__main__':
    main()