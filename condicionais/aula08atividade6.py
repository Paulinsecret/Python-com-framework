import random

jokenpo = []

#jokenpo.append('pedra')
jokenpo.append('papel')
#okenpo.append('tesoura')

jogada1 = input('Escolha pedra, pepel ou tesoura:')


jogada2 = random.choice(jokenpo)
print(jogada2)

if jogada2 == jogada1:
    print("Empate!!")
elif jogada2 != jogada1:
    if jogada1 == 'pedra' and jogada2 =='tesoura':
        print("Você ganhou!")
    elif jogada1 == 'tesoura' and jogada2 == 'papel':
        print("Você Ganhou!!")
    elif jogada1 == 'papel' and jogada2 == 'pedra':
        print("Você Ganhou!!!")
    else:
        print("Você perdeu!!!!!")
 
