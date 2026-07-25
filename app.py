import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================
st.set_page_config(
    page_title="Dashboard de Futebol",
    page_icon="⚽",
    layout="wide"
)

# ==========================
# DADOS
# ==========================
dados = {
    "Time": [
        "Flamengo",
        "Palmeiras",
        "Grêmio",
        "São Paulo",
        "Corinthians",
        "Internacional",
        "Atlético-MG",
        "Fluminense"
    ],
    "Jogos": [20, 20, 20, 20, 20, 20, 20, 20],
    "Vitórias": [14, 13, 11, 10, 8, 9, 12, 7],
    "Empates": [4, 5, 4, 6, 5, 6, 3, 7],
    "Derrotas": [2, 2, 5, 4, 7, 5, 5, 6],
    "Gols": [42, 39, 30, 28, 25, 27, 35, 24]
}

df = pd.DataFrame(dados)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("⚙️ Filtros")

times = st.sidebar.multiselect(
    "Selecione os times",
    options=df["Time"],
    default=df["Time"]
)

df = df[df["Time"].isin(times)]

# ==========================
# TÍTULO
# ==========================
st.title("⚽ Dashboard de Futebol")
st.write("Painel para análise de desempenho dos clubes.")

st.divider()

# ==========================
# MÉTRICAS
# ==========================
c1, c2, c3, c4 = st.columns(4)

c1.metric("🏆 Times", len(df))
c2.metric("⚽ Gols", int(df["Gols"].sum()))
c3.metric("✅ Vitórias", int(df["Vitórias"].sum()))
c4.metric("🎮 Jogos", int(df["Jogos"].sum()))

st.divider()

# ==========================
# GRÁFICOS
# ==========================
col1, col2 = st.columns(2)

with col1:
    fig = px.bar(
        df,
        x="Time",
        y="Gols",
        color="Time",
        text="Gols",
        title="Gols Marcados"
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.pie(
        df,
        names="Time",
        values="Vitórias",
        hole=0.5,
        title="Participação nas Vitórias"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ==========================
# LINHAS
# ==========================
st.subheader("Desempenho dos Clubes")

fig3 = px.line(
    df,
    x="Time",
    y=["Vitórias", "Empates", "Derrotas"],
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)

# ==========================
# RANKING
# ==========================
st.subheader("Ranking de Gols")

ranking = df.sort_values("Gols", ascending=False)

fig4 = px.bar(
    ranking,
    x="Gols",
    y="Time",
    orientation="h",
    color="Gols",
    text="Gols",
)

fig4.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig4, use_container_width=True)

# ==========================
# TABELA
# ==========================
st.subheader("Tabela Completa")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# ==========================
# RODAPÉ
# ==========================
st.markdown("---")
st.caption("Dashboard de Futebol desenvolvido com Streamlit ⚽")