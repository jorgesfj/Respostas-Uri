valores = list(map(str,input().split()))
valores2 = list(map(str,input().split()))
print("VALOR A PAGAR: R$ {:.2f}".format((int(valores[1])*float(valores[2]))+(int(valores2[1])*float(valores2[2]))))