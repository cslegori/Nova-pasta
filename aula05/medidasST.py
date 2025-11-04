import streamlit as st
import math as mt
#Problemas Medidas
TITULO = "Cálculo de área de um quadrado, trângulo e trapézio"
st.title(TITULO)
#Entrada de dados
medidaA = st.number_input("Inserir a medida A:")
medidaB = st.number_input("Inserir a medida B:")
medidaC = st.number_input("Inserir a medida C:")
#Processamento de dados
areaQuadrado = mt.pow(medidaA,2)
areaTriangulo = (medidaA * medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB) / 2
#Saída de Dados
st.write(F"A área do quadrado é: {areaQuadrado:.4f}")
st.write(F"A área do triângulo é: {areaTriangulo:.4f}")
st.write(F"A área do trapézio é: {areaTrapezio:.4f}")
