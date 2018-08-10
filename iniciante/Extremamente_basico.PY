quantidade = int(input())
numeros = list(map(int,input().split()))
lista_razao = []
for i in range(len(numeros)):
	if i+1 < len(numeros):
		razao = lista[i] - lista[i+1]
		lista_razao.append(razao)
print(lista_razao)