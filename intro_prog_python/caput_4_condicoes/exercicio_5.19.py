# Programa 5.19 & 5.20- Contagem de Cédulas
while True:
    valor = float(input("Digite o Valor a pagar: "))
    if valor >= 0.01:
        break

cedulas = 0
atual = 100.0  # Modificado para 100.0 para manter consistência com o tipo de dado
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:  # Adicionado para evitar imprimir cédulas quando não houver
            print(f"{cedulas} Cédula(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 100.0:
            atual = 50.0
        elif atual == 50.0:
            atual = 20.0
        elif atual == 20.0:
            atual = 10.0
        elif atual == 10.0:
            atual = 5.0
        elif atual == 5.0:
            atual = 1.0
        elif atual == 1.0:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0
