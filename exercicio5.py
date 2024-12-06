def exercicios():
    n1 = int(input("digite um numero: "))
    sus = n1 + 1 
    ant = n1 - 1
    raiz = n1 **(1/2)
    qua = n1 ** 2
    cub = n1 ** 3
    print("analisando o valor {}\n o sucessor dele é {}\n o antecessor dele é {}\n a raiz dele é {:.2f}\n ele ao quadrado é {:.2f}\n ele ao cubo é {:.2f}".format(n1, sus, ant, raiz,qua, cub ))
if(__name__ == "__main__"):
    exercicios()