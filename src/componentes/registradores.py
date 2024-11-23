class Registrador:
    def __init__(self, nome, tamanho_em_bits):
        self.nome = nome  # Define o nome do registrador
        self.valor = 0  # Inicializa o valor do registrador com zero
        self.tamanho = tamanho_em_bits  # Define o tamanho do registrador em bits

    def ler(self):
        return self.valor  # Retorna o valor atual do registrador

    def escrever(self, novo_valor):
        self.valor = novo_valor  # Atualiza o valor do registrador com o novo valor

    def __str__(self):
        return f"Registrador {self.nome}: {self.valor}"  # Retorna uma string representando o registrador e seu valor


# Instanciando os registradores
pc = Registrador("PC", 16)  # Contador de Programa
ac = Registrador("AC", 16)  # Acumulador
sp = Registrador("SP", 16)  # Ponteiro de Pilha
ir = Registrador("IR", 16)  # Registrador de Instrução
tir = Registrador("TIR", 16)  # Registrador de Instrução Temporário
r0 = Registrador("0", 16)  # Registrador 0
r_plus1 = Registrador("+1", 16)  # Registrador +1
r_minus1 = Registrador("-1", 16)  # Registrador -1
sm = Registrador("SM", 16)  # Registrador SM
am = Registrador("AM", 16)  # Registrador AM
a = Registrador("A", 16)  # Registrador de uso geral A
b = Registrador("B", 16)  # Registrador de uso geral B
c = Registrador("C", 16)  # Registrador de uso geral C
d = Registrador("D", 16)  # Registrador de uso geral D
e = Registrador("E", 16)  # Registrador de uso geral E
f = Registrador("F", 16)  # Registrador de uso geral F
mar = Registrador("MAR", 16)  # Registrador de Endereço de Memória
mbr = Registrador("MBR", 16)  # Registrador de Buffer de Memória
latch_a = Registrador("Latch A", 16)  # Latch A
latch_b = Registrador("Latch B", 16)  # Latch B
amux = Registrador("AMUX", 16)  # Multiplexador
ula = Registrador("ULA", 16)  # Unidade Lógica Aritmética
deslocador = Registrador("Deslocador", 16)  # Deslocador

# Lista de todos os registradores para fácil acesso
registradores = [
    pc, ac, sp, ir, tir, r0, r_plus1, r_minus1, sm, am,
    a, b, c, d, e, f, mar, mbr, latch_a, latch_b, amux, ula, deslocador
]
