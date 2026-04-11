temperatura = float(input('Qual a temperatura: ')) 

umidade = int(input('Qual a umidade: '))


condicao = (temperatura < 35 and umidade < 70) and 'Condição normal' or 'Condição anormal'

print(condicao)