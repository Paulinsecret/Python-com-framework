notas = True


dados = {
    'notas':[],
    'total':[],
    }
while notas == True:
    dados['notas'].append(int(input("Adcione uma nota:")))
    continuar = input("Deseja adcionar mais notas? s/n")
    if continuar == 's':
        notas = True
    else:
        notas = False
media_aluno1 = sum(dados['notas'])/len(dados['notas'])
print(media_aluno1)
