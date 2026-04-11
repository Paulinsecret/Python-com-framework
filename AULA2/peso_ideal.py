peso = float(input('Coloque seu peso:')) 


altura = float(input('Coloque sua altura: '))


imc = peso / altura ** 2


ideal = imc >= 18.5 and imc <= 24.9 and 'Peso normal' or 'Peso fora do normal'

print(ideal)