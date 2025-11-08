import os
from transformers import pipeline
from collections import Counter 

# 1. Carregamento do Modelo
print("Carregando o modelo facebook/bart-large-mnli... (Aguarde)")
classificador = pipeline(
    "zero-shot-classification", 
    model="facebook/bart-large-mnli"
)
print("Modelo carregado com sucesso.")

# 2. Definição dos Padrões
candidatos_padroes = [
    "Pipe and Filter / Pipeline Architecture",
    "Layered Architecture (MVC or similar)",
    "Microservices Architecture",
    "Monolithic Application"
]

# 3. Definição dos Caminhos
path_do_repositorio = 'Scrapegraph-ai' 
arquivo_saida_txt = 'resultados_analise.txt' 

# 4. Lista para guardar os resultados
resultados_finais = []

# 5. Lógica de Varredura e Análise
try:
    with open(arquivo_saida_txt, 'w', encoding='utf-8') as f:
        
        # Função helper: Imprime na tela E escreve no arquivo .txt
        def log_and_print(message):
            print(message)               # Imprime na tela
            f.write(message + '\n')  # Escreve no arquivo
            f.flush()                # <-- A CORREÇÃO ESTÁ AQUI
        
        # ----- Início da Análise -----
        
        log_and_print(f"### INÍCIO DA ANÁLISE DE ARQUITETURA ###")
        log_and_print(f"Repositório: {path_do_repositorio}")
        log_and_print(f"Modelo: facebook/bart-large-mnli")
        log_and_print("-" * 40)
        
        log_and_print(f"\nIniciando varredura de arquivos .md em: {path_do_repositorio}...")

        # Verifica se o repositório existe antes de continuar
        if not os.path.exists(path_do_repositorio):
            log_and_print(f"\n!!! ERRO CRÍTICO !!!")
            log_and_print(f"A pasta '{path_do_repositorio}' não foi encontrada.")
            log_and_print(f"Verifique se você clonou o repositório para a pasta correta.")
            raise FileNotFoundError(f"Repositório não encontrado em: {path_do_repositorio}")

        for root, dirs, files in os.walk(path_do_repositorio):
            
            if '.git' in dirs:
                dirs.remove('.git')
            if 'venv' in dirs:
                dirs.remove('venv')

            for file in files:
                if file.endswith('.md'):
                    caminho_arquivo = os.path.join(root, file)
                    
                    try:
                        with open(caminho_arquivo, 'r', encoding='utf-8') as doc_file:
                            texto_arquivo = doc_file.read()

                        if len(texto_arquivo.strip()) < 200:
                            log_and_print(f"\n-- Ignorando (muito pequeno): {caminho_arquivo}")
                            continue
                        
                        log_and_print(f"\n== Analisando Arquivo: {caminho_arquivo} ==")
                        
                        resultado = classificador(
                            texto_arquivo, 
                            candidatos_padroes, 
                            multi_label=False
                        )
                        
                        padrao_inferido = resultado['labels'][0]
                        score = resultado['scores'][0]
                        
                        log_and_print(f"Padrão Inferido: {padrao_inferido} (Score: {score:.4f})")
                        
                        for label, score_val in zip(resultado['labels'][1:], resultado['scores'][1:]):
                            log_and_print(f"    - {label}: {score_val:.4f}")

                        resultados_finais.append(padrao_inferido)

                    except Exception as e:
                        log_and_print(f"!! Erro ao ler ou processar {caminho_arquivo}: {e}")

        # 6. Apresentação do Resumo
        log_and_print("\n\n### === RESUMO GERAL DA ANÁLISE DE DOCUMENTAÇÃO === ###")

        if not resultados_finais:
            log_and_print("Nenhum arquivo .md relevante foi encontrado ou processado.")
        else:
            contagem_padroes = Counter(resultados_finais)
            
            log_and_print("Contagem de padrões inferidos (com maior score) nos arquivos .md analisados:")
            for padrao, contagem in contagem_padroes.most_common():
                log_and_print(f"- {padrao}: {contagem} arquivo(s)")

        log_and_print("\nAnálise concluída.")

    print(f"\nSucesso! 🚀 Resultados salvos em: {arquivo_saida_txt}")

except FileNotFoundError as e:
    # Esta mensagem só aparecerá no console
    print(f"\nERRO: {e}")
except IOError as e:
    print(f"ERRO: Não foi possível escrever no arquivo {arquivo_saida_txt}. Verifique as permissões.")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")