from crewai import Task, Crew, Process
from .agents import gerente_setup

# ===============================================================================
# CRIANDO AS TAREFAS
# ===============================================================================

def run_task(input_usuario: str):
    """executa a task de preparação do ambiente apenas via agente."""
    tarefa_setup = Task(
        description=f"""Analise o pedido do usuário: '{input_usuario}'.
Escolha o contexto (Programação, Música ou Jogos) e chame as ferramentas adequadas:
- Programação: VS Code, Documentação, Notion
- Música: Spotify
- Jogos: Steam, Spotify, Discord""",
        expected_output="Confirmação de quais programas foram abertos",
        verbose=False,
        agent=gerente_setup,
    )

    equipe = Crew(
        agents=[gerente_setup],
        tasks=[tarefa_setup],
        process=Process.sequential,
        verbose=False,
    )

    resultado_crew = equipe.kickoff()

    return {
        'descricao': tarefa_setup.description,
        'resultado_crew': str(resultado_crew),
    }
