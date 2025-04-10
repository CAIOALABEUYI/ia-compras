from zipfile import ZipFile
import os

# Estrutura dos arquivos do projeto corrigido
project_files = {
    "ia_compras_pro_v6.py": """
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
        "resposta_indisponivel": \"\"\"Essa pergunta é complexa! Chame o Caio, ele certamente vai saber responder. 
Caso o Caio não saiba, pergunte aos coordenadores Fabi, Denis e João. 
Caso ainda não saibam, conversem com o nosso gerente Marcelo Brito — ele certamente vai saber.
Questões de processos e auditoria? Fale com a Silvia, viu?\"\"\",
        "titulo_chat": "💬 Assistente Interativo (IA de Compras)",
        "pergunta_exemplo": "Ex: Quando é melhor negociar aço inox?"
    },
    "English": {
        "resposta_indisponivel": \"\"\"This is a complex question! Ask Caio, he surely knows the answer.
If he doesn't, ask the coordinators Fabi, Denis, João. 
Still unsure? Our manager Marcelo Brito will know.
For process or audit matters, talk to Silvia.\"\"\",
        "titulo_chat": "💬 Interactive Assistant (Procurement AI)",
        "pergunta_exemplo": "e.g.: When is the best time to negotiate stainless steel?"
    },
    "Français": {
        "resposta_indisponivel": \"\"\"C'est une question complexe ! Demandez à Caio, il connaît sûrement la réponse.
Sinon, contactez les coordinateurs Fabi, Denis, João. 
Toujours pas sûr ? Le directeur Marcelo Brito saura vous répondre.
Pour tout ce qui concerne les processus ou les audits, adressez-vous à Silvia.\"\"\",
        "titulo_chat": "💬 Assistant interactif (IA Achats)",
        "pergunta_exemple": "Ex : Quand négocier l'acier inoxydable ?"
    }
}

# Pergunta assistente na sidebar
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

st.success("✅ IA de Compras carregada com sucesso! Continue navegando nas abas do dashboard para acessar gráficos, KPIs, simulações e relatórios.")
""",
    "requirements.txt": "streamlit\npandas\nmatplotlib\nplotly\nfpdf\n"
}

# Cria o arquivo .zip
zip_path = "/mnt/data/ia_compras_pro_corrigido.zip"
with ZipFile(zip_path, 'w') as zipf:
    for filename, content in project_files.items():
        file_path = f"/mnt/data/{filename}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
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

    qtd = st.slider("Volume", 1, 1000, 100)
    saving_total = (preco_unitario - novo_preco) * qtd
    st.success(f"💸 Economia: R$ {saving_total:,.2f}")

        preco_unitario = st.number_input("Preço Unitário Atual", value=1600.0)

    with col2:
        novo_preco = st.number_input("Novo Preço Negociado", value=1500.0)

    qtd = st.slider("Volume", 1, 1000, 100)
    saving_total = (preco_unitario - novo_preco) * qtd
    st.success(f"💸 Economia: R$ {saving_total:,.2f}")

    saving_total = (preco_unitario - novo_preco) * qtd
    st.success(f"💸 Economia: R$ {saving_total:,.2f}")
