rod = float(input("informe a quantidade de KM que o carro rodou: "))
day = int(input("informe a quantidade de dias que o carro foi utilizado: "))
val = float((rod * 0.15) + (day * 60))
print("o valor do carro fica R$ {:.2f}".format(val))