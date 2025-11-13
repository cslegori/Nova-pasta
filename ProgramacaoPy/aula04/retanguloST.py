import streamlit as st #framework
import math as mt #Biblioteca
#Problema Retangulo
TITULO = "Problema Retangulo"
st.title(TITULO)
#Entrada de Dados
base = st.number_input("Digite a base do retangulo:", min_value=0.0,format="%.1f")
altura = st.number_input("Digite a altura do retangulo:",min_value=0.0,format="%.1f")
#Processamento de Dados
area = base * altura
perimetro = 2 * base + altura * 2
#diagonal = (base**2 + altura**2)**0.5
x = mt.pow(base,2) + mt.pow(altura,2)
diagonal = mt.sqrt(x)
#Saída de Dados
st.write(f"A area do retangulo é: {area}")
st.write(f"O perimetro do retangulo é: {perimetro}")    
st.write(f"A diagonal do retangulo é: {diagonal:.2f}")