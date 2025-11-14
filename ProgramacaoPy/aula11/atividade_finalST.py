import streamlit as st 

st.title("Atividade Final")

N = int(input("Quantas pessoas serão digitadas? "))
#Lista
nomes = []
idades = []
alturas = []

# Entrada de dados
for i in range(N):
    print(f"Dados da {i+1}ª pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

# Cálculo da altura média
altura_media = sum(alturas) / N

# Percentual de pessoas com menos de 16 anos
menores_16 = [nomes[i] for i in range(N) if idades[i] < 16]
percentual_menores = (len(menores_16) / N) * 100

# Saida de dados
print(f"\nAltura média = {altura_media:.2f}")
print(f"Pessoas com menos de 16 anos: {percentual_menores:.1f}%")

if len(menores_16) > 0:
    print("Nomes das pessoas com menos de 16 anos:")
    for nome in menores_16:
        print(nome)
