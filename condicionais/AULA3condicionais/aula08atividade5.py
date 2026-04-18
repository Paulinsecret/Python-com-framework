salario = float(input("Informe seu salário: "))



inss = salario * 0.11

com_inss = salario - inss

if inss >1500:
    inss = 1500
else: 
    inss = inss

if salario <= 2500:
    print(com_inss)
elif salario >2500 and salario <= 3500:
    total = com_inss * 0.925
    print(total)
elif salario >3500 and salario <= 5000:
    total = com_inss * 0.85
    print(total)
else:
    total = com_inss * 0.72,5
    print(total)