import streamlit as st
#Atividade01 Sequencial - Pagamento e troco de produto
TITULO = "Pagamento de Produto com Troco"
st.set_page_config(page_title=TITULO)
st.title(TITULO)
#Entrada de dados
preco = st.number_input("Digite o preço do produto (R$):", min_value=0.0, step=0.01, format="%.2f", help="Insira o valor do produto em reais")
quantidade = st.number_input("Digite a quantidade de produtos:", min_value=0, step=1, help="Insira a quantidade de unidades do produto")
valor_total = st.number_input("Digite o valor em dinheiro fornecido pelo cliente (R$):", min_value=0.0, step=0.01, format="%.2f", help="Insira o valor em reais entregue pelo cliente para pagamento")
#Processamento dos dados
total = (preco * quantidade) #Calculo do valor total da compra
troco = (valor_total - total) #Calculo do troco
#Saída de dados
st.write(f"Valor total da compra: R$ {total:.2f}")
st.write(f"Troco a ser devolvido: R$ {troco:.2f}")