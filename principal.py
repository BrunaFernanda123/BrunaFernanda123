import tkinter as tk

# Funções para cada botão
def abrir_usuarios():
    print("Usuários clicado")

def abrir_cidades():
    print("Cidades clicado")

def abrir_clientes():
    print("Clientes clicado")

def fechar_app():
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Menu Principal")

# Configuração do tamanho da janela
root.geometry("300x200")

# Criação dos botões
btn_usuarios = tk.Button(root, text="Usuários", command=abrir_usuarios)
btn_cidades = tk.Button(root, text="Cidades", command=abrir_cidades)
btn_clientes = tk.Button(root, text="Clientes", command=abrir_clientes)
btn_fechar = tk.Button(root, text="Fechar", command=fechar_app)

# Posicionamento dos botões na janela
btn_usuarios.pack(pady=10)
btn_cidades.pack(pady=10)
btn_clientes.pack(pady=10)
btn_fechar.pack(pady=10)

# Execução da aplicação
root.mainloop()