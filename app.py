import streamlit as st
import pandas as pd
from calculos import *

st.set_page_config(page_title="Simulador Simples Nacional", layout="wide")
st.title("📊 Simulador Simples Nacional – Fator R")

if "historico" not in st.session_state:
    st.session_state.historico = []

st.sidebar.header("Receita")
receita = st.sidebar.number_input("Receita mensal (R$)", min_value=0.0, step=1000.0)

st.sidebar.header("Cargos")
num = st.sidebar.number_input("Quantidade de cargos", min_value=1, step=1)

cargos = []
for i in range(num):
    st.sidebar.subheader(f"Cargo {i+1}")
    nome = st.sidebar.text_input(f"Nome {i}", value=f"Cargo {i+1}")
    salario = st.sidebar.number_input(f"Salário {i}", min_value=0.0, step=500.0)
    qtd = st.sidebar.number_input(f"Qtd {i}", min_value=1, step=1)
    cargos.append({"nome": nome, "salario": salario, "quantidade": qtd})

if st.button("Calcular"):
    folha_m, folha_a, pessoas = calcular_folha(cargos)
    fator_r = calcular_fator_r(folha_a, receita)
    anexo = definir_anexo(fator_r)
    aliquota = calcular_aliquota_efetiva(receita * 12, anexo)
    das = calcular_das(receita, aliquota)

    st.session_state.historico.append({
        "Receita Mensal": receita,
        "Folha Mensal": folha_m,
        "Pessoas": pessoas,
        "Fator R (%)": fator_r * 100,
        "Anexo": anexo,
        "Alíquota Efetiva (%)": aliquota * 100,
        "DAS Mensal": das,
    })

if st.session_state.historico:
    df = pd.DataFrame(st.session_state.historico)
    st.subheader("📈 Histórico")
    st.dataframe(df.style.format({
        "Receita Mensal": "R$ {:,.2f}",
        "Folha Mensal": "R$ {:,.2f}",
        "DAS Mensal": "R$ {:,.2f}",
        "Fator R (%)": "{:.2f}%",
        "Alíquota Efetiva (%)": "{:.2f}%"
    }))
