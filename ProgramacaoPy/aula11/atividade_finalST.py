import streamlit as st 

st.title("Atividade Final")

def ler_pessoas(n):
    pessoas = []

    for i in range(n):
        print(f"\nDados da {i+1}ª pessoa:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: ").replace(",", "."))

        pessoas.append({
            "nome": nome,
            "idade": idade,
            "altura": altura
        })

    return pessoas


def calcular_altura_media(pessoas):
    return sum(p["altura"] for p in pessoas) / len(pessoas)


def filtrar_menores(pessoas):
    return [p for p in pessoas if p["idade"] < 16]


def main():
    n = int(input("Quantas pessoas serão digitadas? "))

    pessoas = ler_pessoas(n)

    # cálculo da altura média
    altura_media = calcular_altura_media(pessoas)

    # filtragem dos menores de 16
    menores = filtrar_menores(pessoas)
    percentual_menores = (len(menores) / n) * 100

    print(f"\nAltura média: {altura_media:.2f} m")
    print(f"Pessoas com menos de 16 anos: {percentual_menores:.1f}%")

    if menores:
        print("Nomes das pessoas com menos de 16 anos:")
        for p in menores:
            print(p["nome"])
    else:
        print("Não há pessoas com menos de 16 anos.")


