import streamlit as st
import math as mt
st.title("Verificação de Triângulo e Cálculo de Perímetro ou Área")
valor_a = st.number_input("Lado A:", min_value=0.0)
valor_b = st.number_input("Lado B:", min_value=0.0)
valor_c = st.number_input("Lado C:", min_value=0.0)
if st.button("Verificar Triângulo"):
    if (valor_a < valor_b + valor_c) and (valor_b < valor_a + valor_c) and (valor_c < valor_a + valor_b):
        st.write("Os valores formam um triângulo.")
        perimetro = valor_a + valor_b + valor_c
        st.write(f"O perímetro do triângulo é: {perimetro:.2f}")
    else:
        st.write("Os valores não formam um triângulo.")
        area = (valor_b * valor_c) / 2
        st.write(f"A área do triângulo é: {area:.2f}")
          