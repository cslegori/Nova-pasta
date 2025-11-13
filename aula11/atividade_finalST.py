import streamlit as st 

st.title("Atividade Final")
nome = st.text_input("Nome")
idade = st.number_input("Digite a idade",min_value=0, step=1)
altura = st.number_input("Digite a altutra", max_value=2,5)
MAXIMO_PESSOAS = 5
MEDIA = ()

