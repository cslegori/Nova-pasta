#Problema tranagulo sem oop
#Entrada de dados
#Triangulo X
print("Inserir as medidas do Triangulo X")
ax = int(input("digite a media a:"))
bx = int(input("digite a media b:"))
cx = int(input("digite a media c:"))
#Triangulo Y
print("Inserir as medidas do Triangulo Y")
ay = int(input("digite a media a:"))
by = int(input("digite a media b:"))
cy = int(input("digite a media c:"))
#Processamento de dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5
#Condicional para verificar qual triangulo é maior
if areax > areay:
    saida = "a area do triangulo X é maior que a area do triangulo Y"
elif areay > areax:
    saida = "a area do triangulo Y é maior que a area do triangulo X"
else:
    saida = "As areas dos triangulos sao iguais"
#Saida de dados
print(f"A area do tiangulo X = {areax:.1f}")
print(f"A area do tiangulo Y = {areay:.1f}")
print (saida)

