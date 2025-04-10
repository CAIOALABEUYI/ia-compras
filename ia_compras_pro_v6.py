import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title="IA de Compras Pro V6", page_icon="", layout="wide")

language = st.sidebar.selectbox(" Idioma / Language / Langue:", ["Português", "English", "Français"])

idiomas_respostas = {
    "Português": {
        "resposta_indisponivel": """Essa pergunta é complexa! Chame o Caio, ele certamente vai saber responder.
Caso o Caio não saiba, pergunte aos coordenadores Fabi, Denis e João.
Caso ainda não saibam, conversem com o nosso gerente Marcelo Brito — ele certamente vai saber.
Questões de processos e auditoria? Fale com a Silvia, viu?""",
        "titulo_chat": " Assistente Interativo (IA de Compras)",
        "pergunta_exemplo": "Ex: Quando é melhor negociar aço inox?",
        "titulo_simulador": " Simulador de Saving",
        "preco_unitario": "Preço Unitário Atual",
        "novo_preco": "Novo Preço Negociado",
        "volume": "Volume",
        "alerta_preco": " O novo preço está maior ou igual ao preço atual. Revise a negociação.",
        "economia_total": " Economia Total Estimada: R$ {saving_total:,.2f}",
        "dashboard": " Dashboard Geral",
        "simulador": " Simulador",
        "analise_gastos": " Análise de Gastos",
        "fornecedores": " Fornecedores",
        "relatorios": " Relatórios",
        "melhores_praticas": " Melhores Práticas"
    },
    "English": {
        "resposta_indisponivel": """This is a complex question! Ask Caio, he surely knows the answer.
If he doesn't, ask the coordinators Fabi, Denis, João.
Still unsure? Our manager Marcelo Brito will know.
For process or audit matters, talk to Silvia.""",
        "titulo_chat": " Interactive Assistant (Procurement AI)",
        "pergunta_exemplo": "e.g.: When is the best time to negotiate stainless steel?",
        "titulo_simulador": " Saving Simulator",
        "preco_unitario": "Current Unit Price",
        "novo_preco": "New Negotiated Price",
        "volume": "Volume",
        "alerta_preco": " The new price is higher than or equal to the current price. Review the negotiation.",
        "economia_total": " Estimated Total Savings: $ {saving_total:,.2f}",
        "dashboard": " General Dashboard",
        "simulador": " Simulator",
        "analise_gastos": " Spend Analysis",
        "fornecedores": " Suppliers",
        "relatorios": " Reports",
        "melhores_praticas": " Best Practices"
    },
    "Français": {
        "resposta_indisponivel": """C'est une question complexe! Demandez à Caio, il connaît sûrement la réponse.
Sinon, contactez les coordinateurs Fabi, Denis, João.
Toujours pas sûr? Le directeur Marcelo Brito saura vous répondre.
Pour tout ce qui concerne les processus ou les audits, adressez-vous à Silvia.""",
        "titulo_chat": " Assistant interactif (IA Achats)",
        "pergunta_exemplo": "Ex : Quand négocier l'acier inoxydable?",
        "titulo_simulador": " Simulateur d'économies",
        "preco_unitario": "Prix unitaire actuel",
        "novo_preco": "Nouveau prix négocié",
        "volume": "Volume",
        "alerta_preco": " Le nouveau prix est supérieur ou égal au prix actuel. Vérifiez la négociation.",
        "economia_total": " Économies totales estimées : {saving_total:,.2f} €",
        "dashboard": " Tableau de bord général",
        "simulador": " Simulateur",
        "analise_gastos": " Analyse des dépenses",
        "fornecedores": " Fournisseurs",
        "relatorios": " Rapports",
        "melhores_praticas": " Meilleures pratiques"
    }
}

st.sidebar.markdown("---")
st.sidebar.subheader(idiomas_respostas[language]["titulo_chat"])
pergunta = st.sidebar.text_input(idiomas_respostas[language]["pergunta_exemplo"])

respostas_base = {
    # ... (respostas anteriores)
}

if pergunta:
    palavras_chave = pergunta.lower().split()
    resposta_encontrada = False
    for palavra_chave, resposta in respostas_base.items():
        if palavra_chave in palavras_chave:
            st.sidebar.success(resposta)
            resposta_encontrada = True
            break
    if not resposta_encontrada:
        st.sidebar.warning(idiomas_respostas[language]["resposta_indisponivel"])

st.success(idiomas_respostas[language]["dashboard"] + ": IA de Compras carregada com sucesso! Continue navegando nas abas do dashboard para acessar gráficos, KPIs, simulações e relatórios.")

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    idiomas_respostas[language]["dashboard"],
    idiomas_respostas[language]["simulador"],
    idiomas_respostas[language]["analise_gastos"],
    idiomas_respostas[language]["fornecedores"],
    idiomas_respostas[language]["relatorios"],
    idiomas_respostas[language]["melhores_praticas"]
])

# Dados simulados para as abas
data_gastos = pd.DataFrame({
    'Categoria': ['Matéria-prima', 'Transporte', 'Embalagem', 'Serviços'],
    'Gasto': [10000, 5000, 3000, 2000]
})

data_pedidos = pd.DataFrame({
    'Data': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']),
    'Valor Total': [10000, 12000, 9000, 11000, 13000],
    'Quantidade': [100, 120, 90, 110, 130],
    'Status': ['Concluído', 'Em Andamento', 'Pendente', 'Concluído', 'Em Andamento']
})

data_fornecedores = pd.DataFrame({
    'Fornecedor': ['A', 'B', 'C', 'D'],
    'Avaliação': [4.5, 3.8, 4.2, 3.5],
    'Tempo de Entrega (dias)': [7, 10, 8, 12]
})

data_fornecedores_detalhado = pd.DataFrame({
    'Fornecedor': ['A', 'B', 'C'],
    'Faturamento Anual (R$)': [1000000, 1500000, 1200000],
    'Previsão de Crescimento (%)': [10, 15, 8],
    'Representação de Compras (%)': [20, 25, 18],
    'Contatos': ['contatoA@email.com', 'contatoB@email.com', 'contatoC@email.com'],
    'Sócios': ['Sócio 1A, Sócio 2A', 'Sócio 1B', 'Sócio 1C, Sócio 2C, Sócio 3C'],
    'Raio X': ['Empresa A: Descrição completa...', 'Empresa B: Descrição completa...', 'Empresa C: Descrição completa...']
})

data_relatorios = pd.DataFrame({
    'Relatório': ['Gastos por Categoria', 'Avaliação de Fornecedores', 'Economia por Negociação'],
    'Link': ['gastos.pdf', 'fornecedores.pdf', 'economia.pdf']
})

melhores_praticas = {
    "Negociação": [
        "Prepare-se para negociar com informações detalhadas sobre o mercado e os fornecedores.",
        "Estabeleça metas claras e limites para a negociação.",
        "Mantenha um bom relacionamento com os fornecedores, mesmo durante a negociação."
    ],
    "Gestão de Fornecedores": [
        "Monitore o desempenho dos fornecedores regularmente.",
        "Comunique-se de forma clara e aberta com os fornecedores.",
        "Desenvolva planos de contingência para lidar com possíveis problemas."
    ],
    "Análise de Gastos": [
        "Use ferramentas de análise de dados para identificar padrões e oportunidades de economia.",
        "Compartilhe os resultados da análise com as partes interessadas.",
        "Implemente ações para reduzir custos e melhorar a eficiência."
    ]
}

with aba1:
    st.header(idiomas_respostas[language]["dashboard"])
    st.subheader("Acompanhamento de Pedidos")
    fig_pedidos = px.line(data_pedidos, x='Data', y='Valor Total', title='Valor Total de Pedidos ao Longo do Tempo')
    st.plotly_chart(fig_pedidos)

    fig_status = px.bar(data_pedidos, x='Status', y='Quantidade', title='Status dos Pedidos')
    st.plotly_chart(fig_status)

    st.subheader("Análise de Gastos")
    fig_gastos_pizza = px.pie(data_gastos, names='Categoria', values='Gasto', title='Distribuição de Gastos por Categoria')
    st.plotly_chart(fig_gastos_pizza)

    st.subheader("Avaliação de Fornecedores")
    fig_fornecedores_scatter = px.scatter(data_fornecedores, x="valor", y="lead_time", color="categoria")

