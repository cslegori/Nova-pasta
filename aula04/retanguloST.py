import streamlit as st 
#Problema Retangulo
st.title("Problema Retangulo")
#Entrada de Dados
base = st.number_input("Digite a base do retangulo:")
altura = st.number_input("Digite a altur do retangulo:")
#Processamento de Dados
area = base * altura
perimetro = 2 * base + altura * 2
diagonal = (base**2 + altura**2)**0.5
#Saída de Dados
st.write(f"A area do retangulo é: {area}")
st.write(f"O perimetro do retangulo é: {perimetro}")    
st.write(f"A diagonal do retangulo é: {diagonal}")