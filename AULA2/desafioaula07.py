vip = str(input("Você é VIP? sim ou não: "))

compra = float(input("Valor da compra: "))

primeira_mes = str(input("É a primeira compra do mes? sim ou não:"))


cupom = (vip == "sim" and compra >= 200 and primeira_mes == 'sim') and 'Cupom liberado' or 'Sem cupom'

print(cupom)

feedback = str(input("Deixe sua avalização:"))

print("Feedback enviado!!!")