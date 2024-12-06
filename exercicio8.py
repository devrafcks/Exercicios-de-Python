def exercicios():
    mt = float(input("digite uma medida em metros:"))
    print("a medida de {} em metros corresponde:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm".format(mt,mt / 1000, mt / 100, mt /10, mt * 10, mt * 100, mt * 1000 ))
if(__name__ == "__main__"):
    exercicios()