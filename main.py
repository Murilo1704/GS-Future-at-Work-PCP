# main.py

from Competencia import Competencia
from Carreira import Carreira
from Perfil import Perfil
from Avaliador import Avaliador

# --- BANCO DE DADOS GLOBAL (LISTA) ---
BANCO_DE_PERFIS = []

# --- 2. DEFINIÇÃO DE COMPETÊNCIAS (LISTA) ---
COMPETENCIAS = [
    # Técnicas
    Competencia("Lógica de Programação", "tecnica"),
    Competencia("Automação e Scripts", "tecnica"),
    Competencia("Estrutura de Dados", "tecnica"),
    # Comportamentais
    Competencia("Criatividade", "comportamental"),
    Competencia("Colaboração", "comportamental"),
    Competencia("Adaptabilidade", "comportamental"),
]

# --- 3. DEFINIÇÃO DE CARREIRAS (DICIONÁRIO e População da Classe Avaliador) ---

dev_software = Carreira(
    nome="Desenvolvedor de Software",
    descricao="Criação e manutenção de sistemas e aplicações.",
    competencias_necessarias={
        "Lógica de Programação": 0.5,
        "Estrutura de Dados": 0.3,
        "Colaboração": 0.2
    }
)

eng_automacao = Carreira(
    nome="Engenheiro de Automação/DevOps",
    descricao="Otimização de processos e infraestrutura por código.",
    competencias_necessarias={
        "Automação e Scripts": 0.4,
        "Adaptabilidade": 0.4,
        "Lógica de Programação": 0.1
    }
)

designer_solucoes = Carreira(
    nome="Designer de Soluções",
    descricao="Criação de soluções inovadoras para problemas de negócio.",
    competencias_necessarias={
        "Criatividade": 0.5,
        "Colaboração": 0.3,
        "Adaptabilidade": 0.2
    }
)

# Adiciona as carreiras na LISTA estática do Avaliador
Avaliador.adicionar_carreira(dev_software)
Avaliador.adicionar_carreira(eng_automacao)
Avaliador.adicionar_carreira(designer_solucoes)


# --- 4. FUNÇÕES DE UTILIDADE E INTERFACE ---

def validar_email(email: str) -> bool:
    """Verifica se o email possui um formato básico válido."""
    if ' ' in email or email.count('@') != 1:
        return False

    partes = email.split('@')
    usuario = partes[0]
    dominio = partes[1]

    if not usuario or not dominio:
        return False

    return True


def cadastrar_perfil():
    """Função para coletar o nome, RM e email do usuário com validação."""
    print("\n--- Cadastro de Perfil ---")
    nome = input("Digite seu Nome Completo: ")
    rm = input("Digite seu RM: ")

    while True:
        email = input("Digite seu E-mail: ")
        if validar_email(email):
            print(" E-mail validado com sucesso!")
            break
        else:
            print(" E-mail inválido. Verifique espaços, o '@' e o conteúdo. Tente novamente.")

    return Perfil(nome, rm, email)


def avaliar_competencias(perfil: Perfil):
    """Permite ao usuário avaliar suas competências de 0 a 5."""
    print("\n--- Avaliação de Competências (Nota de 0 a 5) ---")
    for comp in COMPETENCIAS:
        while True:
            try:
                nota = int(input(f"Qual a sua nota para '{comp.nome}' (0-5)? "))
                if 0 <= nota <= 5:
                    perfil.adicionar_avaliacao(comp.nome, nota)
                    break
                else:
                    print("Por favor, digite um número entre 0 e 5.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    print("Avaliação concluída com sucesso!")


def exibir_recomendacoes(perfil: Perfil):
    """Gera e exibe as recomendações de carreira e aprimoramento."""

    avaliador = Avaliador()
    recomendacoes_carreira = avaliador.gerar_recomendacoes(perfil)
    sugestoes_aprimoramento = avaliador.gerar_sugestoes_aprimoramento(perfil)

    print("\n=================================================")
    print(f"Resultado da Análise para: {perfil.nome} ")
    print(f"   RM: {perfil.rm} | E-mail: {perfil.email}")
    print("=================================================")

    # Exibe as Top 3 Recomendações de Carreira (TUPLA)
    print("\n### Top 3 Recomendações de Carreira")
    for i, (carreira, adequacao) in enumerate(recomendacoes_carreira[:3]):
        percentual = f"{adequacao * 20:.1f}%"
        print(f"   {i + 1}. **{carreira.nome}** (Adequação: {percentual})")
        print(f"      Descrição: {carreira.descricao}")

    # Exibe as Sugestões de Aprimoramento (LISTA)
    print("\n### 💡 Áreas de Aprimoramento Sugeridas")
    if sugestoes_aprimoramento:
        for sugestao in sugestoes_aprimoramento:
            print(f"   - **{sugestao}** (Nota baixa, foco na melhoria!)")
    else:
        print("   - Excelente! Suas notas estão altas. Continue assim!")

    print("\n=================================================")


def buscar_perfil():
    """Busca um perfil cadastrado pelo RM ou E-mail no BANCO_DE_PERFIS."""
    if not BANCO_DE_PERFIS:
        print("\nO banco de dados de perfis está vazio. Cadastre um perfil primeiro.")
        return

    print("\n--- Buscar Perfil ---")
    criterio = input("Digite o RM ou E-mail do perfil que deseja buscar: ").strip()

    perfil_encontrado = None

    # Itera sobre a LISTA do BANCO_DE_PERFIS
    for perfil in BANCO_DE_PERFIS:
        if perfil.rm == criterio or perfil.email.lower() == criterio.lower():
            perfil_encontrado = perfil
            break

    if perfil_encontrado:
        print(f"\nPerfil de {perfil_encontrado.nome} encontrado!")
        exibir_recomendacoes(perfil_encontrado)
    else:
        print(f"\nPerfil não encontrado com o critério: '{criterio}'.")


def cadastrar_e_analisar_perfil():
    """Executa o fluxo completo de cadastro, avaliação, salva e exibe a análise."""

    # 1. Cadastra e avalia
    perfil = cadastrar_perfil()
    avaliar_competencias(perfil)

    # 2. Salva o perfil completo no banco de dados (LISTA)
    BANCO_DE_PERFIS.append(perfil)

    print(f"\nPerfil de **{perfil.nome}** salvo no banco de dados!")

    # 3. Exibe a análise
    exibir_recomendacoes(perfil)
    print("--------------------------------------------------")


def menu_principal_corporativo():
    """Menu principal com loop para gerenciar perfis (CLI)."""

    print("=================================================")
    print("  ⭐ Future Skills Lab - Sistema de Recrutamento  ")
    print("=================================================")

    while True:  # Loop infinito para manter o sistema rodando
        print("\n--- MENU PRINCIPAL ---")
        print("1 - ➕ Cadastrar Novo Perfil e Avaliar")
        print("2 - 🔍 Buscar Perfil Cadastrado e Reexibir Análise")
        print("3 - 🚪 Sair do Sistema")

        escolha = input("Selecione uma opção (1, 2 ou 3): ").strip()

        if escolha == '1':
            cadastrar_e_analisar_perfil()
        elif escolha == '2':
            buscar_perfil()
        elif escolha == '3':
            print("\nObrigado por utilizar o Future Skills Lab. Encerrando o sistema.")
            break  # Sai do loop while
        else:
            print("\nOpção inválida. Por favor, digite 1, 2 ou 3.")


# Bloco de execução principal
if __name__ == "__main__":
    menu_principal_corporativo()