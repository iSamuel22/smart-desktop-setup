"""Tasks e Crew para orquestração do Smart Desktop Setup."""
from crewai import Task, Crew, Process
from .agents import gerente_setup, _classify_contexto
from .tools import abrir_vscode, abrir_spotify, abrir_steam, abrir_documentacao


def _executar_contexto(contexto: str) -> list:
    """Executa as ferramentas apropriadas baseado no contexto."""
    resultados = []
    
    try:
        if contexto == 'programacao':
            resultados.append(abrir_vscode.invoke({}))
            resultados.append(abrir_documentacao.invoke({}))
        elif contexto == 'musica':
            resultados.append(abrir_spotify.invoke({}))
        elif contexto == 'jogos':
            resultados.append(abrir_steam.invoke({}))
            resultados.append(abrir_spotify.invoke({}))
    except Exception as e:
        resultados.append(f"Erro ao executar ferramentas: {str(e)}")
    
    return resultados


# ===============================================================================
# CRIANDO AS TAREFAS
# ===============================================================================

def run_task(input_usuario: str):
    """Executa a task de preparação do ambiente."""
    
    # classifica o contexto
    contexto = _classify_contexto(input_usuario)
    
    # define a tarefa
    tarefa_setup = Task(
        description=f"""Analise o pedido do usuário: '{input_usuario}'. 
Identifique qual é o contexto (Programação, Música ou Jogos) e abra os programas desse contexto:
- Se for programação: abra VS Code e Documentação
- Se for música: abra Spotify
- Se for jogos: abra Steam, Spotify e Discord""",
        expected_output="Confirmação de quais programas foram abertos",
        verbose=False,
        agent=gerente_setup,
    )
    
    # aqui criamos a equipe (crew)
    equipe = Crew(
        agents=[gerente_setup],
        tasks=[tarefa_setup],
        process=Process.sequential,
        verbose=False,
    )
    
    # executa o crew
    resultado_crew = equipe.kickoff()
    
    # executa as ações
    resultados = _executar_contexto(contexto)
    
    return {
        'descricao': tarefa_setup.description,
        'contexto': contexto,
        'resultados': resultados,
        'resultado_crew': str(resultado_crew),
    }
