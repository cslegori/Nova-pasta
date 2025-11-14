import triangualoOOP as tl 
#Instanciar a classe
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()
#Entrada de dados
print("Digite as medidas do triangulo X")
trianguloX.a = int(input("digite a medida a:"))
trianguloX.b = int(input("digite a medida b:"))
trianguloX.c = int(input("digite a medida c:"))
print("Digite as medias do triangulo Y")
trianguloY.a = int(input("Digite a medida a:"))
trianguloY.b = int(input("Digite a medida b:"))
trianguloY.c = int(input("Digite a medida c:"))
#Processamento de dados
areax = trianguloX.area()
areay = trianguloY.area()
#Condicional para verificar qual triangulo é maior
if areax > areay:
    saida = "A area do triangulo X é maior que a area do triangulo Y"
elif areay > areax:
    saida = "A area do triangulo Y é maior que a area do triangulo X"
else:
    saida = "As areas dos triangulos X e Y são iguais"
#saida de dados
print(f"A area do triangulo X = {areax:.f1}")
print(f"A area do triangulo Y = {areay:.f1}")
print(saida)



