def exercicios():
    cart = float(input("quantos reais quer converter? R$"))
    dol =float( cart / 4.96)
    eur = float( cart / 5.37)
    print("a conversão de R${:.2f} para dollar é US${:.2f} e para euro é EUR{:.2f}".format(cart,dol, eur))
if(__name__ == "__main__"):
    exercicios()