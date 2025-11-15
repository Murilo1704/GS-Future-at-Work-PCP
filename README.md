# GS-Future-at-Work-PCP
Sistema Python para análise de perfis e orientação de carreiras GS 2025. Modela Competências, Perfis e Carreiras usando Classes, Listas e Dicionários. O Avaliador usa média ponderada para calcular a adequação do perfil às carreiras do futuro e sugere áreas de melhoria. Interface CLI para gestão de banco de perfis (cadastro/busca).
# 🌟 Global Solution 2025.2: Future Skills Lab - Ferramenta Inteligente de Orientação de Carreiras

## 📌 Descrição do Projeto e Propósito

[cite_start]Este projeto foi desenvolvido para a disciplina de **Pensamento Computacional e Automação com Python** (1º Ano) da FIAP, como parte da **Global Solution 2025.2 - Future at Work**. [cite: 2, 4]

[cite_start]O objetivo principal é criar um sistema em **Python Orientado a Objetos (OOP)** que simule uma ferramenta inteligente de análise e orientação de carreiras. [cite: 7, 13, 15]

O sistema atende a três propósitos principais:
1.  [cite_start]**Análise de Perfil:** Coleta dados de um profissional, incluindo autoavaliações em competências técnicas (ex: Lógica de Programação, Automação) e comportamentais (ex: Criatividade, Adaptabilidade). [cite: 8]
2.  **Recomendação Ponderada:** Utiliza uma lógica de **média ponderada** para calcular o grau de adequação do perfil a diferentes trilhas de carreira predefinidas.
3.  [cite_start]**Gestão de Dados:** Atua como um sistema de recrutamento/banco de dados, permitindo o cadastro de **múltiplos perfis** e a busca por meio de um **Menu Principal (CLI)**. [cite: 17]

[cite_start]A proposta conecta a lógica de programação e a automação ao desenvolvimento humano e profissional, alinhando-se ao tema "Future Skills Lab". [cite: 10]

## 📁 Estrutura de Arquivos, Classes e Implementação

[cite_start]O projeto está organizado em módulos e classes para garantir a aplicação correta dos conceitos de Orientação a Objetos (OOP), conforme o requisito 2. O uso de **Listas, Tuplas e Dicionários** é fundamental para a modelagem dos dados (requisito 1). [cite: 13, 14, 15]

| Arquivo | Classe | Função Principal e Uso de Estruturas |
| :--- | :--- | :--- |
| `main.py` | (Controle) | **Orquestração e Interface:** Contém o loop do **Menu Principal (CLI)** e o **BANCO_DE_PERFIS** (uma **Lista** global) que armazena todos os objetos `Perfil` cadastrados. [cite_start]Também inclui a função de **validação de e-mail** rigorosa. [cite: 17, 16] |
| `Perfil.py` | **`Perfil`** | **Modelagem do Candidato:** Armazena dados do usuário (Nome, RM, Email validado) e suas avaliações. As notas são salvas em um **Dicionário** (`self.avaliacoes`), onde a chave é o nome da competência e o valor é a nota (0-5). |
| `Competencia.py` | **`Competencia`** | **Modelo de Habilidade:** Define as características básicas de uma competência (nome e tipo: `tecnica` ou `comportamental`). |
| `Carreira.py` | **`Carreira`** | **Definição da Trilha:** Define uma carreira e armazena as competências-chave exigidas em um **Dicionário** (`competencias_necessarias`), onde os valores representam o **peso** daquela competência para a trilha. |
| `Avaliador.py` | **`Avaliador`** | **Lógica e Processamento:** Contém métodos para gerar recomendações. O método principal calcula a **média ponderada** de adequação. Os resultados da análise são retornados como uma **Lista de Tuplas** `(carreira, pontuacao)`, que é então ordenada. |

## 👤 Desenvolvedores

| Nome Completo | RM |
| Rafael Quattrer Dalla Costa - RM:562052
GUSTAVO CORDEIRO BRAGA - RM: 562247
MURILO JUSTINO ARCANJO - RM:565470

