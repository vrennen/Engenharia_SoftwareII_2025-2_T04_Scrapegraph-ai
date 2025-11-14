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

# 2. Definição dos Caminhos
path_do_repositorio = 'Scrapegraph-ai'
pastas_relevantes = [
    os.path.join(path_do_repositorio, 'scrapegraphai', 'graphs'),
    os.path.join(path_do_repositorio, 'scrapegraphai', 'nodes')
]


arquivo_saida_txt = os.path.join('Resultados', 'resultados_analise_SUMARIZACAO_T5.txt')

# Lista para guardar todos os resumos gerados para a conclusão final
todos_os_resumos = []

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
            log_and_print("!! Verifique se você rodou o script da pasta raiz.")
            exit()

        # Varredura de Arquivos
        for pasta in pastas_relevantes:
            log_and_print(f"\n\n--- Varrendo Pasta: {pasta} ---")
            
            for root, dirs, files in os.walk(pasta):
                for file in files:
                    if file.endswith('.py') and file != '__init__.py':
                        
                        caminho_arquivo = os.path.join(root, file)
                        log_and_print(f"\n== Analisando Arquivo: {caminho_arquivo} ==")
                        
                        try:
                            with open(caminho_arquivo, 'r', encoding='utf-8') as doc_file:
                                texto_arquivo = doc_file.read()

                            if len(texto_arquivo.strip().split('\n')) < 5:
                                log_and_print("-- Ignorando (muito pequeno).")
                                continue
                            
                            # Prefixo para o T5
                            texto_com_prefixo = "summarize: " + texto_arquivo
                            
                            # Gera o resumo
                            summary = summarizer(texto_com_prefixo, max_length=150, min_length=20, truncation=True)
                            resumo_texto = summary[0]['summary_text']
                            
                            log_and_print(f"--- RESUMO GERADO (T5-SMALL) ---")
                            log_and_print(resumo_texto)

                            # Guarda o resumo na lista para análise posterior
                            todos_os_resumos.append(resumo_texto.lower())

                        except Exception as e:
                            log_and_print(f"!! Erro ao processar {caminho_arquivo}: {e}")

        # ---  GERAÇÃO DA CONCLUSÃO AUTOMÁTICA ---
        
        log_and_print("\n" + "="*50)
        log_and_print("### CONCLUSÃO AUTOMÁTICA DA IA ###")
        log_and_print("="*50)

        if not todos_os_resumos:
            log_and_print("Nenhum resumo foi gerado. Não é possível concluir.")
        else:
            # Contagem de palavras-chave nos resumos gerados
            qtd_pipeline = sum('pipeline' in s for s in todos_os_resumos)
            qtd_node = sum('node' in s for s in todos_os_resumos)
            qtd_graph = sum('graph' in s for s in todos_os_resumos)
            total_arquivos = len(todos_os_resumos)

            log_and_print(f"Total de arquivos analisados: {total_arquivos}")
            log_and_print(f"\nFrequência de termos arquiteturais encontrados nos resumos:")
            log_and_print(f"- Termo 'pipeline': encontrado em {qtd_pipeline} resumos.")
            log_and_print(f"- Termo 'node' (nó): encontrado em {qtd_node} resumos.")
            log_and_print(f"- Termo 'graph' (grafo): encontrado em {qtd_graph} resumos.")

            # Lógica simples de veredito
            log_and_print(f"\n--- VEREDITO DO SCRIPT ---")
            if qtd_pipeline > 0 and qtd_node > 0:
                log_and_print("Baseado nas descrições geradas, a arquitetura detectada é: PIPE AND FILTER.")
                log_and_print("Justificativa: O modelo descreveu repetidamente os componentes como 'nodes' (filtros) organizados em 'pipelines' ou 'graphs'.")
            elif qtd_node > 0:
                log_and_print("Arquitetura sugerida: Baseada em Componentes ou Nós (Indícios de Pipe and Filter).")
            else:
                log_and_print("Resultado inconclusivo baseada apenas nas palavras-chave.")

        log_and_print("\nAnálise de sumarização concluída.")

    print(f"\nSucesso! 🚀 Resultados salvos em: {arquivo_saida_txt}")

except IOError as e:
    print(f"ERRO: Não foi possível escrever no arquivo {arquivo_saida_txt}.")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")