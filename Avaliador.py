# modelo.py (continuando)
from Carreira import Carreira
from Perfil import Perfil
from Competencia import Competencia

class Avaliador:
    """Gera recomendações de carreira e aprimoramento com base no Perfil."""

    CARREIRAS_DISPONIVEIS = []

    @classmethod
    def adicionar_carreira(cls, carreira: Carreira):
        """Método de classe para popular as carreiras disponíveis."""
        cls.CARREIRAS_DISPONIVEIS.append(carreira)

    def gerar_recomendacoes(self, perfil: Perfil) -> list:
        """
        Calcula a pontuação de adequação do perfil a cada carreira.
        Retorna uma lista de tuplas (carreira, pontuacao).
        """
        resultados = []

        for carreira in self.CARREIRAS_DISPONIVEIS:
            pontuacao_total = 0
            peso_total = 0

            for comp, peso in carreira.competencias_necessarias.items():
                if comp in perfil.avaliacoes:
                    nota_perfil = perfil.avaliacoes[comp]
                    pontuacao_total += nota_perfil * peso
                    peso_total += peso

            if peso_total > 0:
                adequacao = pontuacao_total / peso_total
            else:
                adequacao = 0


            resultados.append((carreira, adequacao))


        resultados.sort(key=lambda item: item[1], reverse=True)
        return resultados

    def gerar_sugestoes_aprimoramento(self, perfil: Perfil, limite_nota=3) -> list:
        """Sugere competências com notas abaixo de um limite para aprimoramento."""
        sugestoes = []
        for comp, nota in perfil.avaliacoes.items():
            if nota <= limite_nota:
                sugestoes.append(comp)
        return sugestoes