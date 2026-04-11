t =float(input('Qual a tempratura atual:')) 

u = int(input("Qual a umidade atual: "))

g = int(input("Gás presente? True(1) ou False (0): "))

# o * serve como, se existe verdaeiro e falo (0 ou 1) se for falso entrega 0 pois multiplicou por 0 a questão seguinte, mas se for verdadeiro multiplica por 1 e aparece a questão.
risco =( 
    (t > 40 and u > 80 and g == 1) * 'Nível crítico' or
    (t > 40 and u > 80 and g == 0) and 'Nível alto' or
    (t >=25 and t <=40 and u >= 50 and u <=80 and g == 0) and 'nivel medio' 
    or 'nível baixo'
)
print(risco)
