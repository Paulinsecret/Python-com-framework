compra = float(input("Qual o valor da compra:"))

vip = (input("É vip? True or False:"))

desconto = compra * 0.9

valor_final = (compra > 100 and vip == ('True')) and f"Sua  compra com desconto é de:{desconto}" or f"Você não atendeu aos requisitos de desconto\nSua compra ficou no valor de:{compra}" 

print(valor_final)