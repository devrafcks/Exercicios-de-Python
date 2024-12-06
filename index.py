import ex000
import ex00001
import exercicio1
import exercicio2
import exercicio3
import exercicio4
import exercicio5
import exercicio6
import exercicio7
import exercicio8
import exercicio9
import exercicio10
import exercicio11
import index

def exercicios():

    print("*********************************")
    print("escolha um dos meus projetos :) ")
    print("*********************************")

    proj = int(input("**PROJETOS** \nprojeto de maioridade (1)\nprojeto dia da semana (2)\nprojeto nome (3)\nprojeto data(4)\nprojeto de soma (5)\nprojeto de tipos (6)\nprojeto de contas (7)\nprojeto de conta 2 (8)\nprojeto de nota do INSA (9)\nprojeto de medidas (10)\nprojeto da tabuada (11)\nprojeto de conversão do real (12)\nprojeto da tinta (13)\nDigite qual gostaria de ver:"))
    
    if (proj == 1):
        print("você escolheu projeto de maioridade!")
        ex000.exercicios()
        if ():
            index.exercicios()
    elif (proj == 2):
        print("você escolheu projeto dia da semana!")
        ex00001.exercicios()
        
    elif (proj == 3):
        print("você escolheu projeto nome!")
        exercicio1.exercicios()
        
    elif (proj == 4):
        print("você escolheu projeto data!")
        exercicio2.exercicios()
        
    elif (proj == 5):
        print("você escolheu projeto de soma!")
        exercicio3.exercicios()
        
    elif (proj == 6):
        print("você escolheu projeto de tipos!")
        exercicio4.exercicios()
        
    elif (proj == 7):
        print("você escolheu projeto de contas!")
        exercicio5.exercicios()
        
    elif (proj == 8):
        print("você escolheu projeto de conta 2!")
        exercicio6.exercicios()
        
    elif (proj == 9):
        print("você escolheu projeto de nota do INSA!")
        exercicio7.exercicios()
        
    elif (proj == 10):
        print("você escolheu projeto de medida!")
        exercicio8.exercicios()
        
    elif (proj == 11):
        print("você escolheu projeto da tabuada!")
        exercicio9.exercicios()
        
    elif (proj == 12):
        print("você escolheu projeto de conversão do real")
        exercicio10.exercicios()
    
    elif (proj == 13):
        print("você escolheu projeto da tinta!")
        exercicio11.exercicios()
    else: index.exercicios()
    
if(__name__ == "__main__"):
    exercicios()