def exercicios():
    lar    =  float(input("informe a largura da parede: "))
    alt    =  float(input("informe a altura da parede: "))
    area   =  lar * alt
    tinta  =  area / 2

    print("a área da parede é de {:.1f}m²\nPara pintar essa parede precisará de {:.0f}L de tinta".format(area, tinta))
if(__name__ == "__main__"):
    exercicios()
