#dias da semana
def exercicios():
    
    dom = 1
    seg = 2
    ter = 3
    qua = 4
    qui = 5
    sex = 6 
    sab = 7
    dia = int(input("qual o dia da semana?\n(ex: 1 = domingo, 2 = segunda, etc...) \n"))
    if dia == dom:
        print("hoje é domingo!")
    elif dia == seg:
        print("hoje é segunda!")
    elif dia == ter:
        print("hoje é terça!")
    elif dia == qua:
        print("hoje é quarta!")
    elif dia == qui:
        print("hoje é quinta!")
    elif dia == sex:
        print("hoje é sexta!")
    elif dia == sab:
        print("hoje é sabado!")
    else:
        print("valor invalido!!!")
if(__name__ == "__main__"):
    exercicios()