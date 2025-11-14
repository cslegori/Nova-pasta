PI = 3.14
#Entrda de dados
raio = float(input("digite o valor do raio:"))
#Processamento de dados
circunferencia = 2 * PI * raio
volume = (4/3) * PI * raio **3
area = PI * raio ** 2
#Saida de dados
print(f'''Circunferencia: {circunferencia:.2f}
      Area: {area:.2f}
      PI: {PI}
      ''')