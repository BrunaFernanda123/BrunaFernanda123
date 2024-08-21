import tkinter
from tkinter import *

class Login:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()
        self.titulo = Label (self.janela, text="Informe os Dados")
        self.titulo["font"] = ("Arial", 30, "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()


        self.idUsuarioLabel = Label(self.janela2, text="idUsuario:", font=self.fontePadrao,width=10)
        self.idUsuarioLabel.pack(side=LEFT)
        self.idUsuario = Entry(self.janela2)
        self.idUsuario["width"] = 25
        self.idUsuario["font"] = self.fontePadrao
        self.idUsuario.pack(side=LEFT)

        self.buscar = Button(self.janela2,)
        self.buscar.pack(side=LEFT)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "12")
        self.buscar["width"] = 7
        self.buscar["command"] = self.buscar
        self.buscar.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontePadrao,width=10)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 25
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.telefoneLabel = Label(self.janela4, text="Telefone:", font=self.fontePadrao,width=10)
        self.telefoneLabel.pack(side=LEFT)
        self.telefone= Entry(self.janela4)
        self.telefone["width"] = 25
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack(side=LEFT)

        self.emailLabel = Label(self.janela5, text="Email:", font=self.fontePadrao,width=10)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 25
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.usuarioLabel = Label(self.janela6, text="Usuário:", font=self.fontePadrao,width=10)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.janela6)
        self.usuario["width"] = 25
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontePadrao,width=10)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 25
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.inserir = Button(self.janela8)
        self.inserir["text"] = "Inserir"
        self.inserir["font"] = ("Calibri", "12")
        self.inserir["width"] = 14
        self.inserir.pack(side=LEFT)

        self.alterar = Button(self.janela8)
        self.alterar["text"] = "Alterar"
        self.alterar["font"] = ("Calibri", "12")
        self.alterar["width"] = 14
        self.alterar.pack(side=LEFT)

        self.excluir = Button(self.janela8)
        self.excluir["text"] = "Excluir"
        self.excluir["font"] = ("Calibri", "12")
        self.excluir["width"] = 14
        self.excluir.pack(side=LEFT)


root = Tk()
Login(root)
root.mainloop()