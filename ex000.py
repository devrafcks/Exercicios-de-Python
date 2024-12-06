def exercicios():
    ano = int(input("em que ano estamos? "))
    nasc = int(input("em que ano você nasceu? "))
    idade = int(ano - nasc)

    print("em {} você terá {} anos".format(ano, idade))
    if(idade >= 21):
        print("você terá atingido a maioridade")
    else: 
        print("você não terá atingido a maioridade")
if(__name__ == "__main__"):
    exercicios()
