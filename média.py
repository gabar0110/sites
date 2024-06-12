import streamlit as st
st.title(" my average calculator:")
#add barra lateral
st.sidebar.header("choose the numbers:")
numero1 = st.sidebar.number_input("Número 1",value=0)
numero2 = st.sidebar.number_input("Número 2",value=0)
#add botâo
botao_calcular = st.sidebar.button("calcular média")
st.write(f"Némero 1{numero1}")
st.write(f"numero 2{numero2}")
#executar a ação do botâo
if botao_calcular:
    media = (numero1+numero2)/2
    st.success(f" a média é: {media}")
