lado1 = int(input("Lado menor: "))

lado2 = int(input("Lado mediano : "))

lado3 = int(input("Lado maior: "))

soma = lado1 + lado2


if soma > lado3:
    print('É triângulo:')
else: 
    print('Não é triâgulo')

if lado1 and lado2 == lado3:
    print("Equilatero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Escaleno")
else:
    print("É isóceles")