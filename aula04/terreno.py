#Problema terreno
#Declaração de variavel
largura: float
comprimento: float
#Entrada de dados
largura=float(input("Digite a largura do terreno: "))
comprimento=float(input("Digit  e o comprimento do terreno: "))
valor_metro_quadrado=float(input("Digite o valor do metro quadrado do terreno em reais: "))
#Processamento de dados
area=largura*comprimento
custo=area*valor_metro_quadrado
#Saida de dados
print(f"A area do terreno é de {area}")
print(f"O custo total do terreno é de {custo} reais.")  