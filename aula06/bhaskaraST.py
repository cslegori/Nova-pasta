import streamlit as st
from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt,pow
#Função python
def calculo(delta):
    valor = (sqrt(delta)) / (2*a)
    return valor
#Função Python
header('Calculadora de Bhaskara')
write("Calculadora de raízes \n de uma equação de segundo grau")
write("ax² + bx + c = 0")
#Entrada de Dados
a = text_input('Digite o valor de a:')
b = text_input('Digite o valor de b:')
c = text_input('Digite o valor de c:')
#Processamento de dados
if button('Calcular raízes'):
    try:
       a=float (a)
       b=float (b)
       c=float (c)
       delta = pow(b,2) - 4*a*c
       if delta <0:
        warning("A equação não possui raízes reais")
       elif delta == 0:
        raiz = (-b + calculo(delta))
       else:
        raiz1 = (-b + calculo(delta))
        raiz2 = (-b - calculo(delta))
        success(f"As raízes da equação são: \n Raiz 1:{raiz1} \n Raiz 2: {raiz2}")
    except ValueError:
        error("por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
        error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")