# vip = str(input("Você é VIP? sim ou não: "))
# compra = float(input("Valor da compra: "))
# primeira_mes = str(input("É a primeira compra do mes? sim ou não:"))

# cupom = (vip == "sim" and compra >= 200 and primeira_mes == 'sim') and 'Cupom liberado' or 'Sem cupom'

# print(cupom)
# feedback = str(input("Deixe sua avalização:"))
# print("Feedback enviado!!!")


dados = {
    'vip' : 0,
    'valor_compra' : 0,
    'primeira_compra' : 0,
    'reclamacao' : 0
}

vip = (input('VIP - sim ou nao'))
valor_compra = float(input('R$'))
primeira_compra = input('primeira compra sim ou  nao')
reclamacao = bool(input('True or False'))

dados['primeira_compra'] = primeira_compra
dados['valor_compra'] = valor_compra
dados['primeira_compra'] = primeira_compra
dados['reclamacao'] = reclamacao

v1 = [dados['vip']] == 'sim'
v2 = [dados['valor_compra']] > 200
v3 = [dados['reclamacao']] == False
v4 = [dados['primeira_compra']] == 'sim'

verificacao = (v1 and v2 and v3 and v4) * 'Cupom liberado' or 'Sem cupom'

print(verificacao)


