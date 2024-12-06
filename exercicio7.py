def exercicios():
    m1 = float(input("digite a nota da mensal: "))
    t2 = float(input("digite a nota da trimestral: "))
    m3 = float(input("digite a nota da multi: "))
    t4 = float(input("digite a nota do trabalho: "))
    m = (((m1 + (t2 * 2)) + m3) + t4 ) / 5
    print("a nota final do trimestre foi: {:.1f} ".format(m))
if(__name__ == "__main__"):
    exercicios()