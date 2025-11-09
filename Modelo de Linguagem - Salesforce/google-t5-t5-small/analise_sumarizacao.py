import os
from transformers import pipeline
import torch

# 1. Carregamento do Modelo
MODEL_NAME = "t5-small"
print(f"Carregando modelo: {MODEL_NAME}... (Aguarde)")

try:
    summarizer = pipeline(
        "summarization", 
        model=MODEL_NAME,
        tokenizer=MODEL_NAME
    )
except Exception as e:
    print(f"ERRO CRÍTICO ao carregar o modelo: {e}")
    exit()

print("Modelo carregado com sucesso.")

# --- INÍCIO DA CORREÇÃO ---

# 2. Definição dos Caminhos
# Esta é a ÚNICA pasta que precisamos definir.
# O script AGORA assume que ele está na MESMA pasta que o 'Scrapegraph-ai'
path_do_repositorio = 'Scrapegraph-ai'

# Estas são as pastas DENTRO do repo que são RELEVANTES
pastas_relevantes = [
    os.path.join(path_do_repositorio, 'scrapegraphai', 'graphs'),
    os.path.join(path_do_repositorio, 'scrapegraphai', 'nodes')
]

arquivo_saida_txt = 'resultados_analise_SUMARIZACAO_T5.txt'

# --- FIM DA CORREÇÃO ---

# 3. Lógica de Leitura e Sumarização
try:
    with open(arquivo_saida_txt, 'w', encoding='utf-8') as f:
        
        def log_and_print(message):
            print(message)
            f.write(message + '\n')
            f.flush()
        
        log_and_print(f"### INÍCIO DA ANÁLISE DE SUMARIZAÇÃO (Modelo: {MODEL_NAME}) ###")
        log_and_print(f"Repositório: {path_do_repositorio}")
        log_and_print("-" * 40)

        if not os.path.exists(path_do_repositorio):
            log_and_print(f"!! ERRO CRÍTICO: Pasta '{path_do_repositorio}' não encontrada.")
            log_and_print("!! Verifique se o script está na mesma pasta que o repositório clonado.")
            exit()

        # Agora, vamos varrer as pastas relevantes que definimos
        for pasta in pastas_relevantes:
            log_and_print(f"\n\n--- Varrendo Pasta: {pasta} ---")
            
            # os.walk vai encontrar todos os arquivos
            for root, dirs, files in os.walk(pasta):
                for file in files:
                    # Queremos apenas arquivos .py que não sejam '__init__'
                    if file.endswith('.py') and file != '__init__.py':
                        
                        caminho_arquivo = os.path.join(root, file)
                        log_and_print(f"\n== Analisando Arquivo: {caminho_arquivo} ==")
                        
                        try:
                            with open(caminho_arquivo, 'r', encoding='utf-8') as doc_file:
                                texto_arquivo = doc_file.read()

                            if len(texto_arquivo.strip().split('\n')) < 5:
                                log_and_print("-- Ignorando (muito pequeno).")
                                continue
                            
                            texto_com_prefixo = "summarize: " + texto_arquivo
                            
                            summary = summarizer(texto_com_prefixo, max_length=150, min_length=20, truncation=True)
                            
                            resumo_texto = summary[0]['summary_text']
                            
                            log_and_print(f"--- RESUMO GERADO (T5-SMALL) ---")
                            log_and_print(resumo_texto)

                        except Exception as e:
                            log_and_print(f"!! Erro ao processar {caminho_arquivo}: {e}")

        log_and_print("\n\nAnálise de sumarização concluída.")

    print(f"\nSucesso! 🚀 Resultados salvos em: {arquivo_saida_txt}")

except IOError as e:
    print(f"ERRO: Não foi possível escrever no arquivo {arquivo_saida_txt}.")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")