# 🚀 Atividade 1: Análise de Padrões Arquiteturais com LLMs
**Repositório da Atividade:** `Engenharia_SoftwareII_2025-2_T04_Scrapegraph-ai`

## 👥 Componentes da Equipe

| Nome | Matrícula | Contribuição |
| :--- | :--- | :--- |
| Maria Eduarda M. da Silva | 202300038860 | Documentação, Validação Manual e Scripts |
| Rafael Gomes Oliveira Santos | 202300095730 | Documentação, Validação Manual e Scripts |
| Cauan Teixeira Machado | 202300038627 | Análise com Modelo 1 (facebook/bart-large-mnli) |
| Pedro Joaquim Silva Silveira | 202300038897 | Análise com Modelo 1 (facebook/bart-large-mnli) |
| Breno Silva do Nascimento | 202300038968 | Análise com Modelo 2 (microsoft/unixcoder-base) |
| José Gabriel R. G. de Almeida | 202300095599 | Análise com Modelo 2 (microsoft/unixcoder-base) |
| José Victor Ribeiro de Jesus | 202300038799 | Análise com Modelo 3 (t5-small) |
| Mateus da Silva Barreto | 202300038879 | Análise com Modelo 3 (t5-small) |

---

## 🎯 1. Visão Geral do Projeto

Este projeto cumpre os requisitos da Atividade 1 da disciplina de Engenharia de Software II. O objetivo foi analisar o repositório open-source **`Scrapegraph-ai`** (`https://github.com/ScrapeGraphAI/Scrapegraph-ai`) para identificar seus padrões arquiteturais de software.

Para isso, utilizamos três Modelos de Linguagem (LLMs) distintos da plataforma Hugging Face, com três estratégias de análise diferentes:

1.  **Análise de Documentação (Texto):** Classificação de arquivos `.md` para entender a *intenção* da arquitetura.
2.  **Análise de Código (Quantitativa):** Classificação vetorial de arquivos `.py` para identificar o padrão de código *dominante*.
3.  **Análise de Código (Qualitativa):** Sumarização de arquivos `.py` chave para *validar* as descobertas.

A análise conclusiva, baseada nos modelos de código, determinou que o `Scrapegraph-ai` é predominantemente implementado usando o padrão **Pipe and Filter**.

---

## 🛠️ 2. Tutorial de Execução e Replicabilidade

Este tutorial detalha o passo a passo para configurar o ambiente e executar os três scripts de análise que produzem os logs de resultado.

### 2.1. Estrutura de Pastas

Para que os scripts funcionem, a estrutura de pastas do projeto **deve** ser a seguinte: 

📁 [Pasta Raiz do Projeto] │ ├── 📁 Scrapegraph-ai\ (O repositório clonado) │ ├── 📁 venv\ (O ambiente virtual Python) │ ├── 📜 analise_documentacao.py (Script do Modelo 1) ├── 📜 analise_codigo_alternativa.py (Script do Modelo 2) └── 📜 analise_sumarizacao_FINAL.py (Script do Modelo 3)

### 2.2. Configuração do Ambiente

1.  **Clonar o Repositório Alvo:** Na pasta raiz do seu projeto, clone o `Scrapegraph-ai`:
    ```bash
    git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git
    ```

2.  **Criar o Ambiente Virtual:**
    ```bash
    python -m venv venv
    ```

3.  **Ativar o Ambiente Virtual:**
    * **Windows:** `.\venv\Scripts\activate`
    * **macOS/Linux:** `source venv/bin/activate`

4.  **Instalar Bibliotecas:** Com o `(venv)` ativo, instale todas as dependências necessárias:
    ```bash
    python -m pip install transformers torch sentence-transformers scikit-learn sentencepiece
    ```
    > **Nota:** Se a instalação do `torch` falhar no Windows com um erro de "Caminho Longo" (OSError), você deve habilitar o Suporte a Caminhos Longos no Windows e reiniciar o computador antes de tentar novamente.

---

## ⚙️ 3. Execução e Resultados dos Modelos

Abaixo estão os comandos para executar cada script e os resultados detalhados de cada análise.

### Modelo 1: Análise de Documentação (Classificação de Texto)

Este script varre o repositório em busca de arquivos `.md` e os classifica em um dos quatro padrões.

* **Modelo:** `facebook/bart-large-mnli`
* **Script:** `analise_documentacao.py`
* **O que faz:** Lê cada arquivo `.md`, usa o pipeline de "Zero-Shot Classification" para classificar o texto e conta os "votos" para cada padrão.
* **Comando de Execução:**
    ```bash
    python analise_documentacao.py
    ```
* **Arquivo de Saída:** `resultados_analise.txt`

#### 3.1.1. Resultado Detalhado (Modelo 1)

A análise dos 28 arquivos `.md` relevantes resultou em um **empate técnico**:

* **Layered Architecture (MVC or similar):** 9 arquivo(s)
* **Pipe and Filter / Pipeline Architecture:** 9 arquivo(s)
* **Microservices Architecture:** 8 arquivo(s)
* **Monolithic Application:** 2 arquivo(s)

**Conclusão (Inconclusivo):** Este modelo se mostrou **pouco confiável**. A documentação usa termos ambíguos (como "API", "módulo", "serviço") que confundiram o classificador, fazendo-o ver padrões de Microserviços e Camadas onde eles não eram o foco principal.

### Modelo 2: Análise de Código (Classificação Vetorial)

Este script analisa o código-fonte (`.py`) para desempatar a análise anterior, usando similaridade de vetores.

* **Modelo:** `microsoft/unixcoder-base`
* **Script:** `analise_codigo_alternativa.py`
* **O que faz:** Define 4 "protótipos" (descrições) de padrões. Transforma cada arquivo `.py` e cada protótipo em um vetor (embedding). Compara a similaridade de cosseno entre o código e os protótipos, e vota no padrão mais "próximo".
* **Comando de Execução:**
    ```bash
    python analise_codigo_alternativa.py
    ```
* **Arquivo de Saída:** `resultados_analise_CODIGO_Unixcoder.txt`

#### 3.1.2. Resultado Detalhado (Modelo 2)

A análise de 171 arquivos `.py` válidos foi **decisiva e esmagadora**:

* **Pipe and Filter:** 138 arquivo(s)
* **Microservices:** 20 arquivo(s)
* **Monolithic:** 10 arquivo(s)
* **Layered / MVC:** 3 arquivo(s)

**Conclusão (Decisivo):** Este modelo foi **altamente efetivo**. Ao analisar o código-fonte, ele ignorou a ambiguidade da documentação e identificou corretamente que a vasta maioria dos arquivos (exemplos, grafos e nós) implementa o padrão **Pipe and Filter**.

### Modelo 3: Análise de Código (Sumarização)

Este script valida a descoberta do Modelo 2, pedindo a um modelo de sumarização que *descreva* os arquivos mais importantes nas pastas `/graphs` e `/nodes`.

* **Modelo:** `t5-small`
* **Script:** `analise_SUMARIZACAO_T5.py`
* **O que faz:** Varre as pastas cruciais (`/graphs` e `/nodes`) e usa o modelo `t5-small` para gerar um resumo em inglês de cada arquivo `.py` encontrado. Em seguida, analisa a frequência de termos arquiteturais nos resumos.
* **Comando de Execução:**
    ```bash
    python analise_sumarizacao_FINAL.py
    ```
* **Arquivo de Saída:** `resultados_analise_SUMARIZACAO_T5.txt`

#### 3.1.3. Resultado Detalhado (Modelo 3)

O script analisou 57 arquivos e gerou os seguintes dados:

* **Termo 'graph' (grafo):** Encontrado em 33 resumos.
* **Termo 'node' (nó):** Encontrado em 29 resumos.
* **Termo 'pipeline':** Encontrado em 18 resumos.

O modelo descreveu consistentemente a arquitetura:
* **Arquivos em `/graphs`:** Foram descritos como "scraping **pipeline**" (ex: `smart_scraper_graph.py`).
* **Arquivos em `/nodes`:** Foram descritos como "**node** responsible for fetching/parsing" (ex: `fetch_node.py`, `parse_node.py`).

**Conclusão (Confirmatório):** Este modelo foi **altamente efetivo**. Ele validou a arquitetura **Pipe and Filter** não apenas pela presença das palavras-chave, mas pela descrição funcional correta dos componentes (Nós como unidades de processamento e Grafos como pipelines de orquestração).

---

## 📊 4. Comparação e Avaliação

### 4.1. Tabela Comparativa dos Modelos

| Modelo | Tarefa de NLP | Alvo da Análise | Resultado da Identificação | Efetividade |
| :--- | :--- | :--- | :--- | :--- |
| `facebook/bart-large-mnli` | Classificação (Zero-Shot) | Arquivos de Documentação (`.md`) | **Inconclusivo.** Empate técnico (9-9-8) entre Camadas, Pipe/Filter e Microserviços. | **Baixa** |
| `microsoft/unixcoder-base` | Similaridade de Vetores (Embedding) | Código-Fonte (`.py`) | **Decisivo.** Vitória esmagadora (138 votos) para **Pipe and Filter**. | **Alta** |
| `t5-small` | Sumarização | Código-Fonte (Arquivos-Chave) | **Confirmatório.** Identificou os termos "**graph**" (33x), "**node**" (29x) e "**pipeline**" (18x). | **Alta** |

### 4.2. Avaliação de Efetividade (Justificativa)

Conforme a tabela acima, os modelos de análise de código-fonte foram **significativamente mais efetivos** do que o modelo de análise de texto.

* **Menos Efetivo:** O `facebook/bart-large-mnli` (Modelo 1) foi o menos efetivo. Sua análise da documentação foi "envenenada" pela ambiguidade da linguagem humana. Termos como "serviço" (referindo-se à API do OpenAI) e "módulo" (referindo-se a arquivos Python) o levaram a classificar erroneamente os arquivos como Microserviços ou Camadas.
* **Mais Efetivos:** O `microsoft/unixcoder-base` (Modelo 2) foi o mais efetivo para uma identificação *quantitativa*. Ao analisar o código-fonte, ele foi capaz de determinar qual padrão era de fato o mais implementado, resolvendo o empate. O `t5-small` (Modelo 3) foi o complemento perfeito, fornecendo validação *qualitativa* ao descrever a arquitetura exatamente como ela é: uma coleção de **Pipelines (Grafos)** e **Filtros (Nós)**.