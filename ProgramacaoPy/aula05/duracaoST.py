import streamlit as st
#Problema duração de tempo
TITULO = "Calculadora de Duração de Tempo"
st.set_page_config(page_title=TITULO)
st.title(TITULO) 
#Entrada de dados
tempo = st.number_input("Digite o tempo em segundos:", min_value=0, step=1, help="Insira a duração total em segundos para converter em horas, minutos e segundos")
#Processamento dos dados
horas = tempo // 3600 #Calculo das horas
minutos = (tempo % 3600) // 60 #Calculo dos minutos
segundos = tempo % 60 #Calculo dos segundos
#Saída de dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos.")

