import os
from crewai import Agent
from crewai.llm import LLM

from .tools import abrir_notion, abrir_vscode, abrir_spotify, abrir_steam, abrir_documentacao, abrir_discord


def _classify_contexto(input_text: str) -> str:
    """classifica o pedido do usuário em: programacao, musica ou jogos."""
    t = input_text.lower()
    
    if any(k in t for k in ['codar', 'programa', 'programação', 'vs code', 'desenvolv']):
        return 'programacao'
    if any(k in t for k in ['guitarra', 'música', 'musica', 'tocar', 'relaxar']):
        return 'musica'
    if any(k in t for k in ['jogar', 'jogo', 'games', 'steam']):
        return 'jogos'
    
    return 'programacao' # padrão


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
    tools=[abrir_vscode, abrir_spotify, abrir_steam, abrir_documentacao, abrir_discord, abrir_notion],
    llm=llm,
)


def executar_agente(input_text: str) -> list:
    """executa o agente para preparar o ambiente."""
    resultados = []
    contexto = _classify_contexto(input_text)
    
    if contexto == 'programacao':
        resultados.append(abrir_vscode())
        resultados.append(abrir_documentacao())
        resultados.append(abrir_notion())
    elif contexto == 'musica':
        resultados.append(abrir_spotify())
    elif contexto == 'jogos':
        resultados.append(abrir_steam())
        resultados.append(abrir_spotify())
        resultados.append(abrir_discord())
    
    return resultados
