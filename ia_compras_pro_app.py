
import streamlit as st
import random

st.set_page_config(page_title="IA de Compras Pro", page_icon="💼", layout="centered")

# Título
st.markdown("<h1 style='text-align: center; color: #1a3c70;'>🤖 IA de Compras Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Baseada no livro Procurement Book (versão simulada)</p>", unsafe_allow_html=True)
st.markdown("---")

# Entrada do usuário
user_input = st.text_input("Digite sua pergunta sobre negociação, ferramentas ou melhores práticas:")

# Base simulada
knowledge_base = {
    "negociação": [
        "Para negociações estratégicas, é importante utilizar uma abordagem colaborativa e focada em valor de longo prazo.",
        "Considere técnicas como BATNA (Best Alternative to a Negotiated Agreement) para fortalecer sua posição.",
        "Mapeie o perfil do fornecedor e use a Matriz de Kraljic para classificar a criticidade do item antes de negociar.",
    ],
    "ferramentas": [
        "Use RFI (Request for Information) quando precisar entender melhor as opções do mercado.",
        "RFQ (Request for Quotation) é ideal para produtos padronizados onde o preço é o fator decisivo.",
        "O TCO (Total Cost of Ownership) permite avaliar o custo total além do preço inicial: inclui manutenção, transporte, impostos etc.",
        "SRM (Supplier Relationship Management) é útil para gerenciar fornecedores estratégicos com foco em colaboração.",
    ],
    "melhores práticas": [
        "Padronize processos de compras e documente cada etapa para garantir conformidade.",
        "Utilize dados históricos para planejar negociações e prever demandas.",
        "Integre ferramentas de e-Procurement para aumentar a eficiência e transparência.",
        "Invista em treinamentos contínuos para a equipe de compras sobre técnicas de sourcing e compliance.",
    ],
}

# Geração da resposta
def generate_response(user_input: str) -> str:
    user_input_lower = user_input.lower()
    for key, responses in knowledge_base.items():
        if key in user_input_lower:
            return random.choice(responses)
    return "Essa é uma ótima pergunta! No momento ainda estou aprendendo mais sobre esse tópico. Tente reformular ou aguarde a versão completa com o conteúdo do livro."

# Exibição da resposta
if user_input:
    st.markdown("### Resposta da IA:")
    st.success(generate_response(user_input))

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>💼 Desenvolvido com base em melhores práticas de Procurement</p>", unsafe_allow_html=True)
