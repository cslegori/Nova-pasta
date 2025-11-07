import streamlit as st 
def Celsius_Fahrenheit(t):
    return (t * 1.8) + 32
def Celsius_Kelvin(t):
    return temp + 273.15
def F_Celsius(t):
    return (t - 32) * 5/9
def F_Kelvin(t):
    return F_Celsius(t) + 273.15
def K_Celsius(t):
      return t - 273.15
def K_Fahrenheit(t):
        return Celsius_Fahrenheit(K_Celsius(t)) 
#Problema temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("Conversor de Temperatura")
st.sidebar.markdown("Converte a temperatura entre Celsius, Fahrenheit e Kelvin")
#celsius_selecionado = st.sidebar.checkbox("Celsius",key="temp_celsius")
#ahrenheit_selecionado = st.sidebar.checkbox("Fahrenheit",key="temp_fahrenheit")
#kelvin_selecionado = st.sidebar.checkbox("Kelvin",key="temp_Kelvin")
opcao_selecionada = st.sidebar.radio(options=['Celsius', 'Kelvin', 'Fahrenheit'],key="opcao_radio",label="Selecionar")
#Entrada de dados
temp = st.number_input("Valor da temperatura",format="%.2f",step=1.0)
# if celsius_selecionado + fahrenheit_selecionado + kelvin_selecionado > 1:
#         st.sidebar.error("Por favor, selecione apenas uma unidade de tem")
#Processamento de dados
if st.button("Converter",icon= "🌡"):
            if opcao_selecionada in "Celsius":
                    st.write(f"{temp}°C em Fahrenheit:{Celsius_Fahrenheit(temp):.2}°F")
                    st.write(f"{temp}°C em Kelvin: {Celsius_Kelvin(temp):.2f}K")
            elif opcao_selecionada in "Fahrenheit":
                   st.write(f"{temp}°F em Clesius:{F_Celsius(temp):.2f}°C")
                   st.write(f"{temp}°F em Kelvin:{F_Kelvin(temp):.2f}K")
            elif opcao_selecionada in "Kelvin":
                   st.write(f"{temp}°K em Celsius: {K_Celsius(temp):.2f}°C")
                   st.write(f"{temp}°K em Fahrenheit: {K_Fahrenheit(temp):.2f}°F")
