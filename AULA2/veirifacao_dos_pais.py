idade = int(input("Coloque sua idade:"))

autorizacao = (input("Tem auorização?"))

verificacao = (idade >= 18 and autorizacao == bool('True')) and "Pode participar" or "Não pode participar"