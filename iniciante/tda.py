from Fracao import Fracao
n = int(input())
i = 0
while i<=n:
	tda = input()
	lista_tda = tda.split()
	for i in range(len(lista_tda)):
		n1 = int(lista_tda[0])
		d1 = int(lista_tda[2])
		n2 = int(lista_tda[4])
		d2 = int(lista_tda[6])
		if lista_tda[3] == '+':
			aux1 = (n1*d2 + n2*d1) 
			aux2 = d1*d2
			soma = aux1/aux2
		elif lista_tda[3] == '-':
			aux1 = (n1*d2 - n2*d1) 
			aux2 = d1*d2
			soma = aux1/aux2
		elif lista_tda[3] == '*':
			aux1 = (n1*n2)
			aux2 = (d1*d2)
			soma = aux1/aux2
		elif lista_tda[3] == '/':
			aux1 = (n1*d2)
			aux2 = (n2*d1)
			soma = aux1/aux2
		print("{}/{} = {}".format(aux1,aux2,soma))