def exercicios():
    al = input("digite algo: ")
    print("o tipo primitivo desse valor é: {}".format(type(al)))
    print("só tem espaço? ", al.isspace())
    print("tem numeros? ", al.isnumeric())
    print("é alfabetico? ", al.isalpha())
    print("é alphanumerico? ", al.isalnum())
    print("esta em maiusculas? ", al.isupper())
    print("está em minusculas? ", al.islower())
    print("está capitalizada? ", al.istitle())
if(__name__ == "__main__"):
    exercicios()