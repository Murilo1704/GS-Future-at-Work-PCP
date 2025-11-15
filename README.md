# GS-Future-at-Work-PCP
Sistema Python para análise de perfis e orientação de carreiras GS 2025. Modela Competências, Perfis e Carreiras usando Classes, Listas e Dicionários. O Avaliador usa média ponderada para calcular a adequação do perfil às carreiras do futuro e sugere áreas de melhoria. Interface CLI para gestão de banco de perfis (cadastro/busca).


# 🌟 Future Skills Lab - Ferramenta de Orientação de Carreiras (Global Solution 2025.2)

## [cite_start]📌 Descrição do Projeto e Propósito [cite: 19]

[cite_start]Este projeto é um sistema inteligente desenvolvido em Python, utilizando a Programação Orientada a Objetos (OOP), para simular uma ferramenta de **orientação de carreiras e análise de perfis profissionais do futuro** ("Future at Work" [cite: 2]).

**Propósito:** Analisar competências técnicas e comportamentais (como Lógica, Criatividade e Adaptabilidade) e, com base em algoritmos de ponderação, gerar recomendações personalizadas de carreiras e áreas de aprimoramento. O sistema atua como um banco de dados de recrutamento, permitindo o cadastro e a busca de múltiplos candidatos.

## [cite_start]📁 Estrutura de Arquivos e Classes [cite: 21]

O sistema é modular, organizado em classes, e utiliza listas, tuplas e dicionários para a estruturação dos dados[cite: 13, 14].

| Arquivo/Classe | Descrição | Uso de Estruturas |
| :--- | :--- | :--- |
| `main.py` | Ponto de entrada. Contém o menu principal (CLI), a lógica de I/O, a validação de email e o **BANCO_DE_PERFIS** (Lista global). | **Listas, Condicionais** |
| `Perfil.py` | Classe que modela o candidato (nome, RM, email) e armazena suas autoavaliações de competências. | **Classes, Dicionários** |
| `Competencia.py` | Classe base para definir uma habilidade (nome e tipo: técnica/comportamental). | **Classes** |
| `Carreira.py` | Classe para definir uma trilha profissional, incluindo a **descrição** e o **dicionário de pesos** das competências necessárias. | **Classes, Dicionários** |
| `Avaliador.py` | Classe responsável por todo o processamento: calcula a adequação do perfil a cada carreira (média ponderada) e gera sugestões de aprimoramento. | **Classes, Tuplas, Condicionais** |

## [cite_start]🚀 Instruções de Execução [cite: 20]

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Como Rodar o Sistema

1.  **Clone o Repositório:**
    ```bash
    git clone [SEU_LINK_DO_REPOSITORIO]
    cd [SEU_REPOSITORIO]
    ```

2.  **Execute o Arquivo Principal:**
    ```bash
    python main.py
    ```

3.  **Utilize o Menu:** O sistema será iniciado, apresentando o menu principal[cite: 17]:
    * **Opção 1:** Cadastrar e avaliar um novo perfil.
    * **Opção 2:** Buscar um perfil existente pelo RM ou Email.
    * **Opção 3:** Sair.

## 📸 Demonstração 

*(Aqui você pode adicionar prints da tela do terminal em execução ou um link para um vídeo curto no YouTube demonstrando o uso.)*

[Imagem de um exemplo do CLI sendo executado]

## 👤 Desenvolvedores

| Nome Completo | RM |
| :--- | :--- |
| [SEU NOME COMPLETO] | [SEU RM] |
| [Nome do Colega (se houver)] | [RM do Colega (se houver)] |
