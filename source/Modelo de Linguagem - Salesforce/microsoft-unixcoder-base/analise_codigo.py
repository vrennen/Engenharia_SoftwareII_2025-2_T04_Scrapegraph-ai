import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter 
import numpy as np

# 1. Carregamento do Modelo (MODELO NOVO E MAIS ESTÁVEL)
# Este modelo é da Microsoft e é excelente para embeddings de código.
MODEL_NAME = 'microsoft/unixcoder-base' 
print(f"Carregando modelo: {MODEL_NAME}... (Aguarde)")
print("Este modelo é robusto e não deve pedir 'trust_remote_code'.")

try:
    # Esta única linha cuida de tudo
    model = SentenceTransformer(MODEL_NAME)
    
except Exception as e:
    print(f"ERRO CRÍTICO ao carregar o modelo: {e}")
    exit()

print("Modelo carregado com sucesso.")

# 2. PROTÓTIPOS DE ARQUITETURA (Igual antes)
prototipos = {
    "Pipe and Filter": "Code that defines a data processing pipeline, a graph, or a single node/step in a sequence. (código que define um pipeline de processamento de dados, um grafo, ou um único nó/etapa em uma sequência.)",
    "Layered / MVC": "Code for data models, business logic (controller), presentation layer (view), or database utilities. (código para modelos de dados, lógica de negócios (controlador), camada de apresentação (view), ou utilitários de banco de dados.)",
    "Microservices": "Code for an independent service, API endpoint, network communication, or service discovery. (código para um serviço independente, endpoint de API, comunicação de rede, ou descoberta de serviço.)",
    "Monolithic": "A large module with tightly coupled functions, high complexity, and multiple responsibilities. (um módulo grande com funções fortemente acopladas, alta complexidade, e múltiplas responsabilidades.)"
}

labels_prototipos = list(prototipos.keys())
descricoes_prototipos = list(prototipos.values())

print("Gerando embeddings dos protótipos de arquitetura...")

# 3. GERANDO EMBEDDINGS
embeddings_prototipos = model.encode(descricoes_prototipos)
print("Embeddings dos protótipos gerados.")


# 4. Definição dos Caminhos
path_do_repositorio = 'Scrapegraph-ai' 
arquivo_saida_txt = 'resultados_analise_CODIGO_Unixcoder.txt' # Mudei o nome do txt

# 5. Lista para guardar os resultados
resultados_finais = []

# 6. Lógica de Varredura e Análise (Exatamente como antes)
try:
    with open(arquivo_saida_txt, 'w', encoding='utf-8') as f:
        
        def log_and_print(message):
            print(message)
            f.write(message + '\n')
            f.flush()
        
        log_and_print(f"### INÍCIO DA ANÁLISE DE CÓDIGO FONTE (.py) ###")
        log_and_print(f"Repositório: {path_do_repositorio}")
        log_and_print(f"Modelo: {MODEL_NAME}")
        log_and_print("-" * 40)
        
        log_and_print(f"\nIniciando varredura de arquivos .py em: {path_do_repositorio}...")

        if not os.path.exists(path_do_repositorio):
            log_and_print(f"\n!!! ERRO CRÍTICO !!!")
            log_and_print(f"A pasta '{path_do_repositorio}' não foi encontrada.")
            raise FileNotFoundError(f"Repositório não encontrado em: {path_do_repositorio}")

        for root, dirs, files in os.walk(path_do_repositorio):
            
            if '.git' in dirs: dirs.remove('.git')
            if 'venv' in dirs: dirs.remove('venv')
            if '.vscode' in dirs: dirs.remove('.vscode')

            for file in files:
                if file.endswith('.py'):
                    if file == '__init__.py' or file == 'setup.py':
                        continue

                    caminho_arquivo = os.path.join(root, file)
                    
                    try:
                        with open(caminho_arquivo, 'r', encoding='utf-8') as doc_file:
                            texto_arquivo = doc_file.read()

                        if len(texto_arquivo.strip().split('\n')) < 10:
                            log_and_print(f"\n-- Ignorando (muito pequeno): {caminho_arquivo}")
                            continue
                        
                        log_and_print(f"\n== Analisando Arquivo: {caminho_arquivo} ==")
                        
                        # 1. Gera o embedding do CÓDIGO
                        embedding_codigo = model.encode([texto_arquivo])
                        
                        # 2. Calcula a similaridade
                        similaridades = cosine_similarity(embedding_codigo, embeddings_prototipos)
                        
                        # 3. Encontra o vencedor
                        indice_vencedor = np.argmax(similaridades)
                        padrao_inferido = labels_prototipos[indice_vencedor]
                        score = similaridades[0][indice_vencedor]
                        
                        log_and_print(f"Padrão Inferido: {padrao_inferido} (Similaridade: {score:.4f})")
                        
                        for i, label in enumerate(labels_prototipos):
                            if i != indice_vencedor:
                                log_and_print(f"    - {label}: {similaridades[0][i]:.4f}")

                        resultados_finais.append(padrao_inferido)

                    except Exception as e:
                        log_and_print(f"!! Erro ao ler ou processar {caminho_arquivo}: {e}")

        # 7. Apresentação do Resumo
        log_and_print("\n\n### === RESUMO GERAL DA ANÁLISE DE CÓDIGO === ###")

        if not resultados_finais:
            log_and_print("Nenhum arquivo .py relevante foi encontrado ou processado.")
        else:
            contagem_padroes = Counter(resultados_finais)
            
            log_and_print("Contagem de padrões inferidos (com maior similaridade) nos arquivos .py analisados:")
            for padrao, contagem in contagem_padroes.most_common():
                log_and_print(f"- {padrao}: {contagem} arquivo(s)")

        log_and_print("\nAnálise concluída.")

    print(f"\nSucesso! 🚀 Resultados salvos em: {arquivo_saida_txt}")

except FileNotFoundError as e:
    print(f"\nERRO: {e}")
except IOError as e:
    print(f"ERRO: Não foi possível escrever no arquivo {arquivo_saida_txt}.")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")