import os
import google.generativeai as genai
from dotenv import load_dotenv

# carrega sua API Key do .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERRO: Chave não encontrada no .env")
else:
    genai.configure(api_key=api_key)
    
    print("--- MODELOS DISPONÍVEIS PARA VOCÊ ---")
    try:
        for m in genai.list_models():
            # mostra apenas modelos que geram texto (Chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f"Nome exato: {m.name}")
    except Exception as e:
        print(f"Erro ao conectar: {e}")