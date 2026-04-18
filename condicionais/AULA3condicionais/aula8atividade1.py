print('SISTEMA DE NOTAS')


lista_nomes = []
aluno2 = input("Nome do aluno 2:")
aluno1 = input("Nome do aluno 1:")

lista_nomes.append(aluno1)
lista_nomes.append(aluno2)
print(lista_nomes)

print('lista de alunos:', lista_nomes)

notas_aluno1 = [float(input('nota1:')), float(input('nota2:'))]
notas_aluno2 = [float(input('nota1:')), float(input('nota2:'))]

media_aluno1 = sum(notas_aluno1)/len(notas_aluno1)
media_aluno2 = sum(notas_aluno2)/len(notas_aluno2)

print('Aluno', aluno1, 'Media: ',media_aluno1)
print('Aluno', aluno2, 'Media: ',media_aluno2)


if media_aluno1 >= 6:
    print('Aluno aprovado')
elif media_aluno1 < 6 and media_aluno1 >= 4:
    print('Está de recuperação')
else:
    print('Aluno reprovado')



