
class Competencia:
    """Representa uma competência profissional, técnica ou comportamental."""
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo.capitalize()})"