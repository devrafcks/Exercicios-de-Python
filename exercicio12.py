val = float(input("Qual o valor do produto: R$"))
des = float(input("Qual o valor do desconto em porcentagem: %"))
pf = val - (val * des/ 100)
print("O produto de R$ {:.2f} com desconto de {:.0f}(%) vai custar R$ {:.2f}!!".format(val, des, pf))