import time
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

import patch_crewai

from src.tasks import run_task

st.title("Smart Desktop Setup")
st.markdown("Agente CrewAI que automatiza seu ambiente de trabalho")

input_usuario = st.text_input(
    "O que você quer fazer?",
    placeholder="Ex: 'Hora de codar', 'Vou tocar guitarra', 'Quero jogar'"
)

if st.button("Iniciar", type="primary"):
    if not input_usuario.strip():
        st.warning("Digite um pedido válido")
    else:
        with st.spinner("Processando..."):
            time.sleep(0.3)
            resultado = run_task(input_usuario)

        st.subheader("Ação")
        st.info(resultado['descricao'])

        st.success("Agente completou!")
