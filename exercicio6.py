def exercicios():
    n1 = int(input("digite um numero: "))
    print("analisando o numero {}\nO dobro dele é {}\nO triplo é {}\nA raiz é {:.2f}".format(n1, n1 * 2, n1 * 3, n1 **(1/2)))
if(__name__ == "__main__"):
    exercicios()