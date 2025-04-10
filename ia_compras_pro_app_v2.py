import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="IA de Compras Pro", page_icon="💼", layout="wide")

st.sidebar.title("🔍 Navegação")
menu = st.sidebar.radio("Escolha uma seção:", [
    "🧠 Assistente IA",
    "📊 Painel de Ferramentas",
    "📈 Gráfico de TCO",
    "📃 Sobre"
])

# Base simulada de respostas
knowledge_base = {
    "negociação": [
        "Use BATNA para fortalecer sua posição e sempre conheça o perfil do fornecedor.",
        "Negociações colaborativas trazem mais valor em relações de longo prazo.",
    ],
    "ferramentas": [
        "RFI: coleta informações iniciais. RFQ: solicitação de preços. RFP: proposta com solução completa.",
        "Use TCO para avaliar o custo total da aquisição, não apenas o preço." 
    ],
    "melhores práticas": [
        "Padronize processos, registre tudo e use dados históricos em negociações.",
        "Integre ferramentas digitais como e-Procurement e plataformas de SRM."
    ]
}

# Seção 1: Assistente IA
if menu == "🧠 Assistente IA":
    st.title("🧠 Assistente Inteligente de Compras")
    user_input = st.text_input("Digite sua pergunta:")
    if user_input:
        user_input_lower = user_input.lower()
        for key in knowledge_base:
            if key in user_input_lower:
                st.success(random.choice(knowledge_base[key]))
                break
        else:
            st.warning("Ainda estou aprendendo sobre esse tópico. Reformule ou aguarde atualizações.")

# Seção 2: Painel de Ferramentas
elif menu == "📊 Painel de Ferramentas":
    st.title("📊 Ferramentas de Compras")
    st.markdown("""
    **RFI (Request for Information):** usado para levantamento de opções no mercado.

    **RFQ (Request for Quotation):** solicitação formal de preços. Ideal para produtos padronizados.

    **RFP (Request for Proposal):** quando se precisa de uma solução completa, não apenas preço.

    **TCO (Total Cost of Ownership):** avalia o custo total da aquisição: compra, frete, manutenção, impostos.

    **SRM (Supplier Relationship Management):** gestão colaborativa com fornecedores estratégicos.
    """)

# Seção 3: Gráfico TCO
elif menu == "📈 Gráfico de TCO":
    st.title("📈 Análise de TCO (Custo Total de Aquisição)")
    componentes = ["Preço", "Frete", "Impostos", "Manutenção"]
    valores = [1000, 250, 180, 300]  # Dados simulados
    fig, ax = plt.subplots()
    ax.bar(componentes, valores, color='#1a3c70')
    ax.set_ylabel('Valor em R$')
    ax.set_title('Componentes do TCO')
    st.pyplot(fig)

# Seção 4: Sobre
elif menu == "📃 Sobre":
    st.title("📃 Sobre a IA de Compras Pro")
    st.markdown("""
    Esta é uma aplicação de IA voltada para profissionais de compras. Ela reúne:

    - Melhores práticas de Procurement
    - Ferramentas como RFI, RFQ, TCO e SRM
    - Gráficos interativos
    - Base pronta para evoluir com dados reais

    Desenvolvido por Caio com apoio do ChatGPT 🚀
    """)
