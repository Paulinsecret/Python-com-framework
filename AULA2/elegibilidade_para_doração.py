idade = int(input("Qual a sua idade:"))

peso = float(input("Qual o seu peso: "))


pode_doar = (idade >15 and idade <70) and (peso > 50) and 'Você pode doar' or 'Você não pode doar'
# verifiacao_idade = (idade >=16 and idade <=69 ) and 'Idade permitida' or 'Idade não permitida'

# verificacao_peso = (peso >= 50) and "Peso ideal" or "Peso não ideal"

# pode_doar = verifiacao_idade == 'Idade permitida' and verificacao_peso == 'Peso ideal' and 'Você pode doar' or 'Você não pode doar' 

print(pode_doar)