import streamlit as st
def grafico(datsu1, datsu2, datsu3):
    #Apresentação de grafico exibindo lançamento
    st.area_chart([1,2,3,4,5,6,datsu1], use_container_width=True,height=200,color="#eaff00")
    st.area_chart([1,2,3,4,5,6,datsu2], use_container_width=True,height=200,color="#f65200")
    st.area_chart([1,2,3,4,5,6,datsu3], use_container_width=True,height=200,color="#5100ff")
st.title("🎯Simulação de lançamento de Dardos🎯")
'''Simulação de lançamento de tres dardos.
O objetivo do aplicativo é mostrar o dardo com a maior distancia'''
#Entrada de dados
st.header("Inserir as tres distancias dos dardos lançados pelo jogdor")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distancia 1° Dardo",min_value=0)
with coluna2:
    dardo2 = st.number_input("Distancia 2° Dardo",min_value=0)
with coluna3:
    dardo3 = st.number_input("Distancia 3° Dardo",min_value=0)
maior_distancia = max(dardo1,dardo2,dardo3)
#Estrutura de controle de decisao
if (dardo1>dardo2) and (dardo1>dardo3):
    dardo_vencedor = "Dardo 1"
elif(dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "Dardo 2"
elif (dardo3 > dardo1) and (dardo3 > dardo2):
    dardo_vencedor = "Dardo 3"
elif (dardo1 == dardo2) or(dardo1 == dardo3) or (dardo2 == dardo3):
    dardo_vencedor = "Empate"
#Saida de dados
if st.button("Apresentar resultados de lançamento"):
    if dardo_vencedor == "Empate":
        st.write ("Houve empate sem vencedor")
    st.write(f"O dardo com a maior distancia é o {dardo_vencedor} com {maior_distancia}")
    grafico(dardo1,dardo2,dardo3)