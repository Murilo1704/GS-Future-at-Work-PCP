
class Carreira:
    """Define uma carreira e as competências necessárias para ela."""
    def __init__(self, nome: str, descricao: str, competencias_necessarias: dict):
        self.nome = nome
        self.descricao = descricao
        self.competencias_necessarias = competencias_necessarias

    def __str__(self):
        return f"Carreira: {self.nome}"