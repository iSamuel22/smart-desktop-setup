import time
import pyautogui
from crewai.tools import tool
import webbrowser


@tool
def abrir_vscode() -> str:
    """abre o Visual Studio Code para programação e desenvolvimento"""
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Visual Studio Code')
    time.sleep(1)
    pyautogui.press('enter')
    return "VS Code aberto com sucesso"


@tool
def abrir_spotify() -> str:
    """abre o Spotify para reproduzir música"""
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Spotify')
    time.sleep(1)
    pyautogui.press('enter')
    return "Spotify aberto com sucesso"


@tool
def abrir_steam() -> str:
    """abre o Steam para acessar jogos"""
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Steam')
    time.sleep(1)
    pyautogui.press('enter')
    return "Steam aberto com sucesso"


@tool
def abrir_discord() -> str:
    """abre o Discord para comunicação e chat"""
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Discord')
    time.sleep(1)
    pyautogui.press('enter')
    return "Discord aberto com sucesso"


@tool
def abrir_documentacao() -> str:
    """abre o navegador padrão com a documentação do Python"""
    try:
        webbrowser.open('https://docs.python.org/3/')
        return "Documentação Python aberta no navegador padrão"
    except Exception as e:
        return f"Erro ao abrir documentação: {str(e)}"