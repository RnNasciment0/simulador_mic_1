class Memoria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [0] * tamanho  # Inicializa a memória com zeros

    def ler(self, endereco):
        if 0 <= endereco < self.tamanho:
            return self.dados[endereco]
        else:
            raise ValueError("Endereço fora dos limites da memória")

    def escrever(self, endereco, valor):
        if 0 <= endereco < self.tamanho:
            self.dados[endereco] = valor
        else:
            raise ValueError("Endereço fora dos limites da memória")

    def __str__(self):
        return f"Memoria: {self.dados}"

