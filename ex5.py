pista = int(input('Informe o comprimento da pista em metros: \n'))
voltas = int(input('Quantas voltas serão percorridas? \n'))
qtr = int(input('Quantas vezes será reabastecido? \n'))
consumo = int(input('Informe o consumo em KM/l: \n'))
parada1 = voltas /  qtr
reaba1 = parada1 * pista
print('O total de litros até o primeiro abastecimento é: ', reaba1)