import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import io
from datetime import datetime
import plotly.express as px
import base64
from fpdf import FPDF
import random

st.set_page_config(page_title="IA de Compras Pro V6", page_icon="💼", layout="wide")

language = st.sidebar.selectbox("🌐 Idioma / Language / Langue:", ["Português", "English", "Français"])

idiomas_respostas = {
    "Português": {
        "resposta_indisponivel": "Essa pergunta é complexa! Chame o Caio, ele certamente vai saber responder. Caso o Caio não saiba, pergunte aos coordenadores Fabi, Denis, João. Caso ainda não saibam, conversem com o nosso gerente Marcelo Brito — ele certamente vai saber. Questões de processos e auditoria falem com a Silvia, viu?""Essa pergunta é complexa! Chame o Caio, ele certamente vai saber responder.",
        "titulo_chat": "💬 Assistente Interativo (IA de Compras)",
        "pergunta_exemplo": "Ex: Quando é melhor negociar aço inox?"
    },
    "English": {
        "resposta_indisponivel": \"This is a complex question! Ask Caio, he surely knows the answer. If he doesn't, ask the coordinators Fabi, Denis, João. Still unsure? Our manager Marcelo Brito will know. For process or audit matters, talk to Silvia.\",
        "titulo_chat": "💬 Interactive Assistant (Procurement AI)",
        "pergunta_exemplo": "e.g.: When is the best time to negotiate stainless steel?"
    },
    "Français": {
        "resposta_indisponivel": \"C'est une question complexe ! Demandez à Caio, il connaît sûrement la réponse. Si ce n’est pas le cas, demandez aux coordinateurs Fabi, Denis, João. Sinon, notre directeur Marcelo Brito saura répondre. Pour les questions de processus ou d’audit, parlez à Silvia.\",
        "titulo_chat": "💬 Assistant interactif (IA Achats)",
        "pergunta_exemple": "Ex : Quand négocier l'acier inoxydable ?"
    }
}

# Adiciona assistente de perguntas
st.sidebar.markdown("---")
st.sidebar.subheader(idiomas_respostas[language]["titulo_chat"])
pergunta = st.sidebar.text_input(idiomas_respostas[language]["pergunta_exemplo"])
respostas_base = [
    "Negocie aço inox no início do trimestre, quando os fornecedores renovam metas.",
    "Para ar-condicionado, negociações são melhores no inverno, fora da sazonalidade.",
    "Audite fornecedores com base em lead time, qualidade e conformidade documental.",
    "Use índices de mercado e histórico de preços como base para solicitar desconto."
]
if pergunta:
    if any(palavra in pergunta.lower() for palavra in ["aço", "ar-cond", "negociar", "auditar", "desconto"]):
        st.sidebar.success(random.choice(respostas_base))
    else:
        st.sidebar.warning(idiomas_respostas[language]["resposta_indisponivel"])

# 📬 Envio de Relatório por E-mail (simulado)
with st.expander("📬 Enviar Relatório por E-mail"):
    email = st.text_input("Digite o e-mail de destino")
    if st.button("Enviar Relatório"): 
        if email and "@" in email:
            st.success(f"✅ Relatório enviado com sucesso para {email}! (simulado)")
        else:
            st.error("❌ E-mail inválido. Verifique e tente novamente.")

# 🚨 Alertas por Variação de Preço
st.subheader("🚨 Alertas de Variação de Preço")
avaliacoes = pd.DataFrame({
    "Item": ["Fogão Industrial", "Coifa Inox", "Split 36k BTUs"],
    "Último Preço": [1640, 1220, 3250],
    "Preço Atual": [1670, 1215, 3300],
    "Variação %": [round((1670-1640)/1640*100,1), round((1215-1220)/1220*100,1), round((3300-3250)/3250*100,1)]
})

for index, row in avaliacoes.iterrows():
    if abs(row["Variação %"]) > 2:
        st.warning(f"⚠️ {row['Item']} teve variação de {row['Variação %']}%")
    else:
        st.info(f"ℹ️ {row['Item']} com variação de {row['Variação %']}%")

# Organiza tudo em abas para um layout de dashboard completo
abas = st.tabs([
    "🏠 Visão Geral", "📉 Análise de Custos", "📊 Gráficos", "📌 KPIs & Fornecedores",
    "🤖 Assistente", "📤 Exportações", "🚨 Alertas", "💰 Simulações"
])

with abas[0]:
    st.title("🏠 Visão Geral")
    st.markdown("Visualize os principais dados estratégicos de compras indiretas da sua operação.")
    st.dataframe(df)

with abas[1]:
    st.header("📉 Análise de Custos")
    st.dataframe(df)
    selected = st.selectbox("Equipamento para gráfico de custo", df["Equipamento"])
    selected_row = df[df["Equipamento"] == selected].iloc[0]
    custo_componentes = {
        "Matéria-prima": selected_row["Matéria-prima"],
        "Mão de Obra": selected_row["Mão de Obra"],
        "Margem": (selected_row["Custo Total Estimado"] - selected_row["Matéria-prima"] - selected_row["Mão de Obra"])
    }
    fig, ax = plt.subplots()
    ax.pie(custo_componentes.values(), labels=custo_componentes.keys(), autopct='%1.1f%%')
    ax.axis('equal')
    st.pyplot(fig)

with abas[2]:
    st.header("📊 Gráficos e Tendências")
    st.subheader("Pareto de Custos")
    df_pareto = df.sort_values("Custo Total Estimado", ascending=False)
    fig_pareto = px.bar(df_pareto, x="Equipamento", y="Custo Total Estimado", title="Pareto dos Custos")
    st.plotly_chart(fig_pareto)

    st.subheader("Evolução de Preços")
    preco_tempo = pd.DataFrame({
        "Data": pd.date_range(end=datetime.today(), periods=6, freq='M'),
        "Fogão": [1590, 1600, 1610, 1625, 1630, 1640],
        "Coifa": [1180, 1195, 1200, 1210, 1215, 1220],
        "Split": [3100, 3150, 3180, 3200, 3220, 3250]
    })
    preco_tempo.set_index("Data", inplace=True)
    st.line_chart(preco_tempo)

    st.subheader("Comparação de Fornecedores")
    comparador = pd.DataFrame({
        "Fornecedor": ["Venâncio", "Progás", "Metalcubas"],
        "Preço Médio": [1625, 1580, 1680],
        "Prazo Entrega": [12, 14, 10],
        "SLA %": [90, 92, 95]
    })
    fig_bar = px.bar(comparador, x="Fornecedor", y=["Preço Médio", "SLA %"], barmode="group")
    st.plotly_chart(fig_bar)

with abas[3]:
    st.header("📌 KPIs e Fornecedores")
    st.subheader("🏭 Fornecedores Sugeridos")
    st.dataframe(fornecedores)
    st.subheader("📌 KPIs por Item")
    st.dataframe(kpis)

with abas[4]:
    st.header("🤖 Assistente Interativo")
    st.sidebar.markdown("---")
    st.sidebar.subheader(idiomas_respostas[language]["titulo_chat"])
    pergunta = st.sidebar.text_input(idiomas_respostas[language]["pergunta_exemplo"])
    if pergunta:
        if any(palavra in pergunta.lower() for palavra in ["aço", "ar-cond", "negociar", "auditar", "desconto"]):
            st.sidebar.success(random.choice(respostas_base))
        else:
            st.sidebar.warning(idiomas_respostas[language]["resposta_indisponivel"])

with abas[5]:
    st.header("📤 Exportações")
    st.download_button("📥 Baixar Excel com Custos Estimados", data=csv, file_name="custos.csv", mime="text/csv")
    export_md = df.to_markdown(index=False)
    b64 = base64.b64encode(export_md.encode()).decode()
    href = f'<a href="data:text/markdown;base64,{b64}" download="relatorio_compras.md">📄 Baixar relatório em Markdown</a>'
    st.markdown(href, unsafe_allow_html=True)

    if st.button("📄 Gerar Relatório em PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório IA de Compras Pro", ln=True, align="C")
        for i, row in df.iterrows():
            pdf.cell(200, 10, txt=f"{row['Equipamento']} - Custo Total: R$ {row['Custo Total Estimado']:.2f}", ln=True)
        pdf_path = "/mnt/data/relatorio_compras_pro.pdf"
        pdf.output(pdf_path)
        with open(pdf_path, "rb") as file:
            st.download_button("📥 Baixar PDF", data=file, file_name="relatorio_compras_pro.pdf", mime="application/pdf")

    with st.expander("📬 Enviar Relatório por E-mail"):
        email = st.text_input("Digite o e-mail de destino")
        if st.button("Enviar Relatório"):
            if email and "@" in email:
                st.success(f"✅ Relatório enviado com sucesso para {email}! (simulado)")
            else:
                st.error("❌ E-mail inválido. Verifique e tente novamente.")

with abas[6]:
    st.header("🚨 Alertas de Variação de Preço")
    for index, row in avaliacoes.iterrows():
        if abs(row["Variação %"]) > 2:
            st.warning(f"⚠️ {row['Item']} teve variação de {row['Variação %']}%")
        else:
            st.info(f"ℹ️ {row['Item']} com variação de {row['Variação %']}%")

with abas[7]:
    st.header("💰 Simulador de Saving")
    col1, col2 = st.columns(2)
    with col1:
        preco_unitario = st.number_input("Preço Unitário Atual", value=1600.0)
    with col2:
        novo_preco = st.number_input("Novo Preço Negociado", value=1500.0)
    qtd = st.slider("Volume", 1, 1000, 100)
    saving_total = (preco_unitario - novo_preco) * qtd
    st.success(f"💸 Economia: R$ {saving_total:,.2f}")