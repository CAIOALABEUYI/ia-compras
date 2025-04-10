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
    "aço": "Para negociar aço inox, o ideal é monitorar os preços de mercado e as tendências de oferta e demanda. Negociações no início do trimestre, quando fornecedores renovam suas metas, podem render descontos significativos.",
    "ar-condicionado": "A melhor época para negociar ar-condicionado é durante o inverno, fora da alta temporada. Fornecedores costumam oferecer descontos para aumentar as vendas durante os meses de baixa procura. Além disso, fique atento a promoções de modelos de anos anteriores, que podem ter preços mais competitivos.",
    "auditar": "A auditoria de fornecedores deve ser baseada em critérios como lead time, qualidade dos produtos/serviços e conformidade documental. Utilize checklists e ferramentas de avaliação para garantir um processo completo.",
    "desconto": "Para solicitar descontos, use índices de mercado e histórico de preços como base. Apresente dados concretos que justifiquem sua solicitação e esteja preparado para negociar com base no volume de compra e prazos de pagamento.",
    "saving cost breakdown": "Saving Cost Breakdown é uma análise detalhada dos custos economizados em um projeto ou negociação. Permite identificar onde as economias foram feitas e como elas impactaram o resultado final.",
    "rfi": "RFI (Request for Information) é um documento usado para coletar informações gerais sobre fornecedores e seus produtos/serviços. É útil na fase inicial de um processo de compra para identificar potenciais fornecedores.",
    "rfp": "RFP (Request for Proposal) é um documento usado para solicitar propostas detalhadas de fornecedores. Inclui requisitos específicos e critérios de avaliação para ajudar na seleção do melhor fornecedor.",
    "rfq": "RFQ (Request for Quotation) é um documento usado para solicitar cotações de preços de fornecedores. Geralmente usado quando os requisitos são bem definidos e o foco é o preço.",
    "cost avoidance": "Cost Avoidance refere-se às ações tomadas para evitar custos futuros. Inclui negociações de preços, otimização de processos e outras estratégias para reduzir gastos.",
    "spend analysis": "Spend Analysis é a análise dos gastos de uma empresa para identificar padrões, oportunidades de economia e áreas de melhoria. Ajuda a otimizar o processo de compras e reduzir custos.",
    "análise swot": "A Análise SWOT (Forças, Fraquezas, Oportunidades e Ameaças) é uma ferramenta usada para avaliar a posição estratégica de uma empresa ou projeto. Ajuda a identificar áreas de melhoria e oportunidades de crescimento.",
    "curva abc": "A Curva ABC é uma ferramenta usada para classificar itens de estoque ou fornecedores com base em seu valor ou importância. Ajuda a priorizar recursos e otimizar o gerenciamento de estoque."
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

data_relatorios = pd.DataFrame({
    'Relatório': ['Gastos por Categoria', 'Avaliação de Fornecedores', 'Economia por Negociação'],
    'Link': ['gastos.pdf', 'fornecedores.pdf', 'economia.pdf']
})

melhores_praticas = [
    "Negocie sempre com múltiplos fornecedores para obter melhores preços.",
    "Mantenha um bom relacionamento com seus fornecedores para garantir entregas e condições favoráveis.",
    "Analise seus gastos regularmente para identificar oportunidades de economia.",
    "Utilize ferramentas de análise de dados para tomar decisões mais informadas."
]

with aba1:
    st.header(idiomas_respostas[language]["dashboard"])
    # Adicionar KPIs e gráficos resumidos aqui
    st.write("Aqui você pode adicionar KPIs e gráficos resumidos.")

with aba2:
    st.header(idiomas_respostas[language]["titulo_simulador"])
    col1, col2 = st.columns(2)

    with col1:
        preco_unitario = st.number_input(idiomas_respostas[language]["preco_unitario"], value=1600.0)

    with col2:
        novo_preco = st.number_input(idiomas_respostas[language]["novo_preco"], value=1500.0)

    qtd = st.slider(idiomas_respostas[language]["volume"], 1, 1000, 100)

    if novo_preco >= preco_unitario:
        st.warning(idiomas_respostas[language]["alerta_preco"])
    else:
        saving_total = (preco_unitario - novo_preco) * qtd
        st.success(idiomas_respostas[language]["economia_total"].format(saving_total=saving_total))
        # Adicionar visualização do saving aqui
        st.write("Aqui você pode adicionar uma visualização do saving.")

with aba3:
    st.header(idiomas_respostas[language]["analise_gastos"])
    fig_gastos = px.bar(data_gastos, x='Categoria', y='Gasto', title='Gastos por Categoria')
    st.plotly_chart(fig_gastos)

with aba4:
    st.header(idiomas_respostas[language]["fornecedores"])
    st.subheader("Avaliação de Fornecedores")
    fornecedor = st.selectbox("Selecione o Fornecedor", ["Fornecedor A", "Fornecedor B", "Fornecedor C"])
    qualidade = st.slider("Qualidade do Produto/Serviço", 1, 5, 3)
    prazo = st.slider("Prazo de Entrega", 1, 5, 3)
    comunicacao = st.slider("Comunicação", 1, 5, 3)
    preco = st.slider("Preço", 1, 5, 3)
    st.write(f"Avaliação do Fornecedor {fornecedor}:")
    st.write(f"- Qualidade: {qualidade}/5")
    st.write(f"- Prazo de Entrega: {prazo}/5")
    st.write(f"- Comunicação: {comunicacao}/5")
    st.write(f"- Preço: {preco}/5")

with aba5:
    st.header(idiomas_respostas[language]["relatorios"])
    st.table(data_relatorios)

with aba6:
    st.header(idiomas_respostas[language]["melhores_praticas"])
    for pratica in melhores_praticas:
        st.write(f"- {pratica}")
