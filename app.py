import streamlit as st

# Configurações da página
st.set_page_config(page_title="A Jornada dos Dados", page_icon="📊")

# Cabeçalho
st.title("🐑 A Jornada dos Dados")

# Imagem da Ovelha Mend
st.image("img/ovelha_mend.png", width=250)

# Narrativa inicial
st.markdown("""
Você acorda em uma biblioteca antiga, coberta por poeira e silêncio...  
Em cima da mesa, um envelope selado com cera:

**“Convocação urgente! O Reino dos Dados está em perigo.”**

Com a ajuda da Ovelha Mend, você deve restaurar o conhecimento perdido!
""")

# Escolha do jogador
escolha = st.radio("O que você quer fazer?", ["📜 Abrir o envelope", "😴 Voltar a dormir"])

if escolha == "📜 Abrir o envelope":
    st.success("Você aceita o desafio! A Ovelha Mend aparece para te guiar.")
    st.image("img/ovelha_mend_feliz.png", width=250)
    st.markdown("**Missão:** descubra o que é uma variável quantitativa!")

    resposta = st.radio("Qual das opções é uma variável quantitativa?", [
        "Cor dos olhos", "Número de filhos", "Tipo de animal", "Estado civil"
    ])

    if resposta == "Número de filhos":
        st.balloons()
        st.success("Acertou! Variáveis quantitativas são expressas em números.")
        st.markdown("🔓 Nova fase desbloqueada em breve!")
    else:
        st.warning("Tente de novo! Dica: pense em algo que você possa contar.")

elif escolha == "😴 Voltar a dormir":
    st.warning("Você volta a dormir... e o Reino dos Dados continua em perigo 😢")
