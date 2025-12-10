import os
from crewai import Agent
from crewai.llm import LLM

from .tools import abrir_vscode, abrir_spotify, abrir_steam, abrir_discord, abrir_documentacao, abrir_notion


# ===============================================================================
# CRIANDO O AGENTE
# ===============================================================================

# configura gemini como LLM usando CrewAI LLM
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY não configurada no arquivo .env")

llm = LLM(
    model="gemini-2.5-flash",
    provider="google",
    api_key=api_key,
)

# agente: gerente de setup
gerente_setup = Agent(
    role='Gerente de Setup',
    goal='Preparar o ambiente de trabalho do usuário abrindo os programas corretos',
    backstory="""Você é um assistente pessoal eficiente que interpreta comandos do usuário
e abre os programas necessários para o contexto (programação, música ou jogos).""",
    verbose=False,
    allow_delegation=False,
    tools=[abrir_vscode, abrir_spotify, abrir_steam, abrir_discord, abrir_documentacao, abrir_notion],
    llm=llm,
)
