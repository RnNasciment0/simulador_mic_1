import tkinter as tk
from tkinter import scrolledtext
from src.componentes.registradores import Registrador, registradores
from src.componentes.memoria import Memoria
from src.alu import ALU

# Variável de estado para rastrear se a ação foi realizada
acao_realizada = False

# Função para alternar entre fazer e desfazer a ação
def alternar_acao():
    global acao_realizada
    if acao_realizada:
        desfazer_acao()
    else:
        fazer_acao()
    acao_realizada = not acao_realizada

# Função para fazer a ação
def fazer_acao():
    registradores_label.config(text="Ação realizada")

# Função para desfazer a ação
def desfazer_acao():
    registradores_label.config(text="Ação desfeita")

# Função para exibir o conteúdo dos registradores
def exibir_registradores():
    texto = "\n".join(str(reg) for reg in registradores)
    registradores_label.config(text=texto)

# Função para exibir o conteúdo da memória
def exibir_memoria():
    texto = str(memoria)
    memoria_text.delete(1.0, tk.END)
    memoria_text.insert(tk.END, texto)

# Função para realizar uma operação na ALU
def operar_alu():
    operacao = operacao_entry.get()
    operando1 = int(operando1_entry.get())
    operando2 = int(operando2_entry.get())
    resultado = alu.operar(operacao, operando1, operando2)
    resultado_label.config(text=f"Resultado: {resultado}")

# Função para ler um valor da memória
def ler_memoria():
    endereco = int(memoria_endereco_entry.get())
    valor = memoria.ler(endereco)
    memoria_valor_entry.delete(0, tk.END)
    memoria_valor_entry.insert(0, str(valor))

# Função para escrever um valor na memória
def escrever_memoria():
    endereco = int(memoria_endereco_entry.get())
    valor = int(memoria_valor_entry.get())
    memoria.escrever(endereco, valor)
    exibir_memoria()

# Função para ler um valor de um registrador
def ler_registrador():
    nome = registrador_nome_entry.get()
    for reg in registradores:
        if reg.nome == nome:
            registrador_valor_entry.delete(0, tk.END)
            registrador_valor_entry.insert(0, str(reg.ler()))
            break

# Função para escrever um valor em um registrador
def escrever_registrador():
    nome = registrador_nome_entry.get()
    valor = int(registrador_valor_entry.get())
    for reg in registradores:
        if reg.nome == nome:
            reg.escrever(valor)
            exibir_registradores()
            break

# Cria a janela principal
root = tk.Tk()
root.title("Simulador MIC1")

# Cria um rótulo
label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=0, column=0, columnspan=2, pady=10)

# Cria um rótulo para exibir os registradores
registradores_label = tk.Label(root, text="Registradores")
registradores_label.grid(row=2, column=0, columnspan=2, pady=10)

# Cria um botão para alternar a ação
button_alternar = tk.Button(root, text="Alternar Ação", command=alternar_acao)
button_alternar.grid(row=3, column=0, columnspan=2, pady=10)

# Cria um rótulo para exibir a memória
memoria_label = tk.Label(root, text="Memória")
memoria_label.grid(row=4, column=0, columnspan=2, pady=10)

# Cria um botão para exibir a memória
button_memoria = tk.Button(root, text="Exibir Memória", command=exibir_memoria)
button_memoria.grid(row=5, column=0, columnspan=2, pady=10)

# Cria um widget de texto rolável para exibir a memória
memoria_text = scrolledtext.ScrolledText(root, width=40, height=10)
memoria_text.grid(row=6, column=0, columnspan=2, pady=10)

# Cria entradas para operação da ALU
operacao_entry = tk.Entry(root)
operacao_entry.grid(row=7, column=0, columnspan=2, pady=5)
operacao_entry.insert(0, "Operação (e.g., ADD)")

operando1_entry = tk.Entry(root)
operando1_entry.grid(row=8, column=0, columnspan=2, pady=5)
operando1_entry.insert(0, "Operando 1")

operando2_entry = tk.Entry(root)
operando2_entry.grid(row=9, column=0, columnspan=2, pady=5)
operando2_entry.insert(0, "Operando 2")

# Cria um botão para realizar a operação na ALU
button_alu = tk.Button(root, text="Operar ALU", command=operar_alu)
button_alu.grid(row=10, column=0, columnspan=2, pady=10)

# Cria um rótulo para exibir o resultado da ALU
resultado_label = tk.Label(root, text="Resultado")
resultado_label.grid(row=11, column=0, columnspan=2, pady=10)

# Cria entradas e botões para leitura e escrita de memória
memoria_endereco_entry = tk.Entry(root)
memoria_endereco_entry.grid(row=12, column=0, pady=5)
memoria_endereco_entry.insert(0, "Endereço")

memoria_valor_entry = tk.Entry(root)
memoria_valor_entry.grid(row=12, column=1, pady=5)
memoria_valor_entry.insert(0, "Valor")

button_ler_memoria = tk.Button(root, text="Ler Memória", command=ler_memoria)
button_ler_memoria.grid(row=13, column=0, pady=5)

button_escrever_memoria = tk.Button(root, text="Escrever Memória", command=escrever_memoria)
button_escrever_memoria.grid(row=13, column=1, pady=5)

# Cria entradas e botões para leitura e escrita de registradores
registrador_nome_entry = tk.Entry(root)
registrador_nome_entry.grid(row=14, column=0, pady=5)
registrador_nome_entry.insert(0, "Nome do Registrador")

registrador_valor_entry = tk.Entry(root)
registrador_valor_entry.grid(row=14, column=1, pady=5)
registrador_valor_entry.insert(0, "Valor")

button_ler_registrador = tk.Button(root, text="Ler Registrador", command=ler_registrador)
button_ler_registrador.grid(row=15, column=0, pady=5)

button_escrever_registrador = tk.Button(root, text="Escrever Registrador", command=escrever_registrador)
button_escrever_registrador.grid(row=15, column=1, pady=5)

# Inicializa a memória e a ALU
memoria = Memoria(256)
alu = ALU()

# Executa a aplicação
root.mainloop()