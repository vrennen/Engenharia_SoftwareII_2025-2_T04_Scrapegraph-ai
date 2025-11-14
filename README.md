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

### 1.1. Justificativa da Escolha do Projeto 

 O `Scrapegraph-ai` foi selecionado como projeto-alvo por ser um exemplo ideal de arquitetura moderna e de um domínio relevante (IA e Web Scraping). Sua estrutura, baseada em "Grafos" e "Nós", sugeria fortemente um padrão arquitetural claro (Pipe and Filter), tornando-o um caso de estudo perfeito para testar se os LLMs conseguiriam identificar esse padrão com precisão.

### 1.2. Links da Atividade

* **Tutorial em PDF:** [PDF Tutorial da atividade](https://drive.google.com/drive/u/1/folders/1yU5Zi8ZS_l8EF2YbSSM_h13qN-sI7DCH)
* **Vídeo Tutorial (YouTube):** [Video Tutorial + Explicativo](https://www.youtube.com/watch?v=XRYl72aVZHw)

---

## 🛠️ 2. Tutorial de Execução e Replicabilidade

Este tutorial detalha o passo a passo para configurar o ambiente e executar os três scripts de análise que produzem os logs de resultado.

### 2.1. Estrutura de Pastas

Esta é a estrutura de pastas do projeto. Os scripts devem ser executados a partir da **pasta raiz** (`ENGENHARIA_SOFT...`).
```
.
├── reports/              # Relatórios finais e logs de execução
│   ├── Resultado_Final.md
│   ├── resultados_analise_CODIGO_Unixcoder.txt
│   ├── resultados_analise_SUMARIZACAO_T5.txt
│   └── resultados_analise.txt
│
├── scripts/              # Scripts de execução de cada modelo
│   ├── facebook-bart-large-mnli/
│   │   └── analise_documentacao.py   (Script 1)
│   ├── google-t5-t5-small/
│   │   └── analise_sumarizacao.py    (Script 3)
│   └── microsoft-unixcoder-base/
│       └── analise_codigo.py         (Script 2)
│
├── Scrapegraph-ai/       # O repositório-alvo clonado
├── venv/                 # Ambiente virtual Python
│
├── README.md             # Este documento
└── requirements.txt      # Arquivo de dependências 
```

### 2.2. Modelos de Linguagem Utilizados (Hugging Face)
* **Modelo 1 (Texto):** [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli)
* **Modelo 2 (Código):** [microsoft/unixcoder-base](https://huggingface.co/microsoft/unixcoder-base)
* **Modelo 3 (Sumarização):** [google-t5/t5-small](https://huggingface.co/google-t5/t5-small)

### 2.3. Configuração do Ambiente

1.  **Clonar o Repositório Alvo:**
    ```bash
    git clone https://github.com/ScrapeGraphAI/Scrapegraph-ai.git
    ```

2.  **Criar e Ativar o Ambiente Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar Bibliotecas :**
    Com o `(venv)` ativo, instale todas as dependências usando o arquivo `requirements.txt`:
    ```bash
    python -m pip install -r requirements.txt
    ```
    > **Nota:** Se a instalação do `torch` falhar no Windows com um erro de "Caminho Longo" (OSError), você deve habilitar o Suporte a Caminhos Longos no Windows e reiniciar o computador.

---

## ⚙️ 3. Execução e Resultados dos Modelos

### Modelo 1: Análise de Documentação (Classificação de Texto)
* **Comando:** `python analise_documentacao.py`
* **Arquivo de Saída:** `resultados_analise.txt`
* **Resultado:** **Inconclusivo** (Empate técnico 9-9-8).

### Modelo 2: Análise de Código (Classificação Vetorial)
* **Comando:** `python analise_codigo_alternativa.py`
* **Arquivo de Saída:** `resultados_analise_CODIGO_Unixcoder.txt`
* **Resultado:** **Decisivo**. Vitória esmagadora do **Pipe and Filter** (138 votos).

### Modelo 3: Análise de Código (Sumarização)
* **Comando:** `python analise_sumarizacao_FINAL.py`
* **Arquivo de Saída:** `resultados_analise_SUMARIZACAO_T5.txt`
* **Resultado:** **Confirmatório**. O modelo descreveu os arquivos usando termos como "pipeline" (18x), "node" (29x) e "graph" (33x).

---

## 📊 4. Comparação e Avaliação

### 4.1. Tabela Comparativa dos Modelos

| Modelo | Tarefa de NLP | Alvo da Análise | Resultado da Identificação | Efetividade |
| :--- | :--- | :--- | :--- | :--- |
| `facebook/bart-large-mnli` | Classificação (Zero-Shot) | Documentação (`.md`) | **Inconclusivo.** Empate técnico (9-9-8). | **Baixa** |
| `microsoft/unixcoder-base` | Similaridade de Vetores (Embedding) | Código-Fonte (`.py`) | **Decisivo.** Vitória (138 votos) para **Pipe and Filter**. | **Alta** |
| `google/t5-small` | Sumarização | Código-Fonte (Arquivos-Chave) | **Confirmatório.** Descreveu "graph" (33x), "node" (29x), "pipeline" (18x). | **Alta** |

### 4.2. Validação Manual e Efetividade 

Para validar os resultados da IA, realizamos uma **análise humana (manual)** do código-fonte, que serviu como nosso "gabarito".

1.  **Análise Manual:** Uma inspeção das pastas `/nodes` e `/graphs` do `Scrapegraph-ai` confirma que a arquitetura é **Pipe and Filter**. Os "Nodes" são os Filtros (tarefas únicas) e os "Graphs" são os Orquestradores (Pipelines) que os conectam.
2.  **Validação dos Modelos:**
    * **Modelo 1 (Texto): REPROVADO.** Falhou por ser "enganado" pela ambiguidade da documentação (palavras como "API" e "módulo").
    * **Modelo 2 (Código): APROVADO.** Ignorou o ruído textual e identificou corretamente o padrão dominante no código, batendo 100% com nosso gabarito.
    * **Modelo 3 (Sumarização): APROVADO.** Validou o Modelo 2, descrevendo qualitativamente os componentes com os termos corretos ("node", "pipeline").

### 4.3. Dificuldades e Limitações Encontradas 

Durante a execução, enfrentamos diversos desafios técnicos que são cruciais para a reprodutibilidade:

* **Falha de Modelos:** As primeiras tentativas com modelos da Salesforce (ex: `codet5p-110m-embedding`) falharam repetidamente com erros de `trust_remote_code` e incompatibilidade de dimensionalidade (`1D vs 2D array`), exigindo a troca para modelos mais robustos.
* **Limitação de Ambiente (Windows):** A instalação do `torch` falhou com um `OSError: No such file or directory`. Isso foi causado pelo limite de 260 caracteres para nomes de caminho no Windows. A correção exigiu a habilitação do "Long Paths Support" no registro do Windows.
* **Bugs de Tokenizer:** O Modelo 2 (`unixcoder-base`), embora bem-sucedido na maioria, falhou em 38 arquivos (ex: `abstract_graph.py`) com um erro de `index out of range`, indicando um bug no tokenizer do modelo ao processar certas sintaxes de Python.

---

## 🖥️ 5. Infraestrutura Utilizada 

 Toda a análise foi executada em um ambiente **Local**. As especificações da máquina utilizada para os testes e geração de resultados foram:

* **CPU:** AMD Ryzen 5 3400G with Radeon Vega Graphics     (3.70 GHz)
* **GPU:** Veneida RX580 8 GB DDR5 AMD
* **Memória RAM:** 24 GB DDR4 32000MhZ
* **Sistema Operacional:** Windows 11 Pro
* **Ambiente:** Python 3.10 (via venv)

---

## 🏁 6. Conclusão Final

A lição final desta atividade é clara: para a análise de arquitetura de software, o **código-fonte é uma fonte de verdade muito mais confiável do que a documentação**. Os modelos de IA treinados especificamente para código (`unixcoder-base` e `t5-small`) são as ferramentas mais adequadas para a tarefa, pois ignoram o "ruído" da linguagem natural e focam na semântica da implementação.