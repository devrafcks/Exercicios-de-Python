val = float(input("Qual o valor do salario do funcionario: R$"))
aum = float(input("Qual o valor do aumento em porcentagem: %"))
pf = val + (val * aum/ 100)
print("O salario desse funcionario de R$ {:.2f} com aumento de {:.0f}(%) vai ficar R$ {:.2f}!!".format(val, aum, pf))