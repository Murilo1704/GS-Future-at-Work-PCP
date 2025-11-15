# modelo.py

# Arquivo: Perfil.py (Atualizar o construtor da classe)

class Perfil:
    """Representa o perfil de um profissional com suas avaliações de competências."""

    def __init__(self, nome: str, rm: str, email: str):
        self.nome = nome
        self.rm = rm
        self.email = email  # <--- Novo atributo
        self.avaliacoes = {}

    def adicionar_avaliacao(self, nome_competencia: str, nota: int):
        """Adiciona ou atualiza a nota de uma competência."""
        if 0 <= nota <= 5:
            self.avaliacoes[nome_competencia] = nota
        else:
            print("Nota inválida. Use um valor de 0 a 5.")

    def exibir_avaliacoes(self):
        """Exibe as notas atuais do perfil."""
        print(f"\n--- Avaliações de Competências de {self.nome} ---")
        for comp, nota in self.avaliacoes.items():
            print(f"- {comp}: {nota}/5")
        print("-------------------------------------------------")