import calculadora as c 
#Instanciacao do objeto
circulo = c.calculadora1()
#Entrada de dados
raio = float(input("Digite o valor de raio: "))
#Processamento de dados
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)
#Saida de dados
print(f'''Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {circulo.PI}
      ''')