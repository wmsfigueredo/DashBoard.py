import streamlit as st 
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(layout="wide", page_title="Análise Socioeconômica")


df = pd.read_csv("Questionario_Socioeconomico.csv", sep=",", decimal=",")

# Sidebar com filtros
st.sidebar.header("Filtros")
with st.sidebar:
    Nome = st.selectbox("Nome", ["Todos"] + list(df["Nome"].unique()))
    Nascimento = st.selectbox("nascimento", ["Todos"] + list(df["Nascimento"].unique()))
    Cidade = st.selectbox("Cidade", ["Todos"] + list(df["Cidade"].unique()))
    Renda = st.selectbox("Renda", ["Todos"] + list(df["Renda"].unique()))
    Periodo = st.selectbox("Periodo", ["Todos"] + list(df["Periodo"].unique()))
    Curso = st.selectbox("Curso", ["Todos"] + list(df["Curso"].unique()))
# Aplicar filtros de forma segura
df_filtered = df.copy()


if Nome != "Todos":
    df_filtered = df_filtered[df_filtered["Nome"] == Nome]  # Filtra o df_filtered, não o df original
    df_filtered
if Nascimento != "Todos":
    df_filtered = df_filtered[df_filtered["Nascimento"] == Nascimento]  # Continua filtrando o resultado anterior
    df_filtered
if Cidade != "Todos":
    df_filtered = df_filtered[df_filtered["Cidade"] == Cidade]
    df_filtered
if Renda != "Todos":
    df_filtered = df_filtered[df_filtered["Renda"] == Renda]
    df_filtered
if Curso != "Todos":
    df_filtered = df_filtered[df_filtered["Curso"] == Curso]
    df_filtered
if Periodo != "Todos":
    df_filtered = df_filtered[df_filtered["Periodo"] == Periodo]
    df_filtered
# Visualização dos dados filtrados
st.header("Dados Filtrados")
st.dataframe(df_filtered)

# Gráficos
st.header("Visualizações")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
with col1:
    fig_renda_periodo = px.bar(df_filtered, x="Periodo", y="Renda", 
                              title="Renda por Período",
                              color="Periodo")
    st.plotly_chart(fig_renda_periodo)

with col2:
    if "Cidade" in df_filtered.columns:
        fig_cidade = px.pie(df_filtered, names="Cidade", 
                           title="Distribuição por Cidade")
        st.plotly_chart(fig_cidade)

with col3:
    if "Nascimento" in df_filtered.columns:
        fig_temporal = px.line(df_filtered, x="Nascimento", y="Renda",
                              title="Evolução Temporal da Renda")
        st.plotly_chart(fig_temporal)

with col4:
    if all(col in df_filtered.columns for col in ["Renda", "Cidade"]):
        fig_box = px.box(df_filtered, x="Cidade", y="Renda",
                        title="Distribuição de Renda por Cidade")
        st.plotly_chart(fig_box)


df_filtered = df_filtered.dropna()
