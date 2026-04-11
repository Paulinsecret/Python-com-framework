idade = int(input('Qual a sua idade: '))


classificacao = idade < 12 and 'Criança' or idade >= 12 and idade <=17 and 'Adolescente' or idade >= 18 and 'Adulto'

print(classificacao)