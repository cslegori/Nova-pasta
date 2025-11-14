import streamlit as st

st.title("Cadastro de Pessoas")

# Número de pessoas
N = st.number_input("Quantas pessoas deseja cadastrar?", min_value=1, step=1)

pessoas = []

st.subheader("Insira os dados:")

for i in range(int(N)):
    st.write(f"### Pessoa {i+1}")
    nome = st.text_input(f"Nome {i+1}", key=f"nome_{i}")
    idade = st.number_input(f"Idade {i+1}", min_value=0, key=f"idade_{i}")
    altura = st.number_input(f"Altura (em metros) {i+1}", min_value=0.0, format="%.2f", key=f"altura_{i}")

    if nome and altura > 0:
        pessoas.append({"nome": nome, "idade": idade, "altura": altura})

st.write("---")

if st.button("Calcular resultados"):
    if len(pessoas) < N:
        st.warning("Preencha todos os dados corretamente antes de calcular.")
    else:
        # Cálculo da altura média
        altura_media = sum(p["altura"] for p in pessoas) / N

        # Pessoas com menos de 16 anos
        menores_16 = [p for p in pessoas if p["idade"] < 16]
        perc_menores = (len(menores_16) / N) * 100

        # Exibição dos resultados
        st.subheader("Resultados")
        st.write(f"**Altura média:** {altura_media:.2f} m")
        st.write(f"**Porcentagem de pessoas com menos de 16 anos:** {perc_menores:.1f}%")

        if menores_16:
            st.write("**Pessoas com menos de 16 anos:**")
            nomes = [p["nome"] for p in menores_16]
            st.write(", ".join(nomes))
        else:
            st.write("Não há pessoas com menos de 16 anos.")