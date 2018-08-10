valores = list(map(float,input().split()	))
a = valores[0]
b = valores[1]
c = valores[2]
area_triangulo_retagulo = (a*c)/2
area_circulo = 3.14159 *(c**2)
area_trapezio = ((a+b)*c)/2
area_quadrado = b**2
area_retangulo = b*a
print("""TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}""".format(area_triangulo_retagulo,area_circulo,area_trapezio,area_quadrado,area_retangulo))