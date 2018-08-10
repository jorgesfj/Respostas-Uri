numero_de_imoveis = int(input())
dicionario = {}
lista = []
lista_imoveis =  []
lista_imoveis.append(numero_de_imoveis)
while numero_de_imoveis!=0:
	pessoas_consumo = input().split()
	dicionario[pessoas_consumo[1]] = pessoas_consumo[0]
	cont = 0
	
	while  cont<numero_de_imoveis-1:
		cont +=1
		pessoas_consumo = input().split()
		dicionario[pessoas_consumo[1]] = pessoas_consumo[0]
	
	print(dicionario)
	
	numero_de_imoveis = int(input())
	lista_imoveis.append(numero_de_imoveis)

for i in range(len(lista_imoveis)):
	for i in range(1,lista_imoveis[i]):
		numerador = i
		denominador = dicionario[lista_imoveis[i]]
		consumo_por_pessoa = numerador//denominador
		dicionario2 = {}
		dicionario2[denominador] = consumo_por_pessoa
for i in range(1,len(lista_imoveis)):
	print('Cidade# {}:'.format(i))
	for i in range(len(dicionario2)):
		print(i,'-',dicionario2[lista_imoveis[i]], end='')