import streamlit as st 
st.title("Pessoa mais velha")
#declaração de variaveis
nome1 = str
idade1 = int
nome2 = str
idade2 = int
#entrada de dados
#Pessoa 1
if st.button("Calcular"):
  
    st.header("Insira os dados das Pessoas")
nome = st.text_input("Nome1:")
idade = st.number_input("Idade1,format=%.1f")
#Pessoa 2
st.header("Insira os dados das Pessoas")
nome = st.text_input("Nome2:")
idade = st.number_input("Idade2,format=%.1f")
if (idade1>idade2):
        pessoa_mais_velha = "Pessoa1"
elif(idade2 > idade1):
        pessoa_mais_velha = "Pessoa 2"


maior_idade = max(idade1,idade2)

#Processamebto de dados
pessoa1 = input("Nome1:")
idade1 = int(input("Idade1:"))
pessoa2 = input("Nome2:")
idade2 = int(input("Idade2:"))

if (idade1>idade2):
        pessoa_mais_velha = "Pessoa1"
elif(idade2 > idade1):
        pessoa_mais_velha = "Pessoa 2"
elif (idade1 == idade2):
        pessoa_mais_velha = "Idades Iguais"

if st.button("Enviar"):

        if pessoa_mais_velha : pessoa1
        elif pessoa_mais_velha : pessoa2
else:
        st.write = pessoa1 
    
#Saida de dados

print(f"Pessoa mais velha é:{pessoa_mais_velha}")