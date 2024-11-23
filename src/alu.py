class ALU:
    def __init__(self):
        self.resultado = 0

    def operar(self, operacao, operando1, operando2):
        if operacao == "ADD":
            self.resultado = operando1 + operando2  # Soma
        elif operacao == "SUB":
            self.resultado = operando1 - operando2  # Subtração
        elif operacao == "MUL":
            self.resultado = operando1 * operando2  # Multiplicação
        elif operacao == "DIV":
            self.resultado = operando1 / operando2  # Divisão
        elif operacao == "AND":
            self.resultado = operando1 & operando2  # Operação AND bit a bit
        elif operacao == "OR":
            self.resultado = operando1 | operando2  # Operação OR bit a bit
        elif operacao == "XOR":
            self.resultado = operando1 ^ operando2  # Operação XOR bit a bit
        elif operacao == "NOT":
            self.resultado = ~operando1  # Operação NOT bit a bit
        elif operacao == "SHL":
            self.resultado = operando1 << operando2  # Deslocamento à esquerda
        elif operacao == "SHR":
            self.resultado = operando1 >> operando2  # Deslocamento à direita
        # Adicione outras operações conforme necessário
        return self.resultado
