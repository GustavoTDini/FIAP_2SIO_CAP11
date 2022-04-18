from tkinter import *
from tkinter import ttk
from simulacao import simular_fila, stop_sim


# Classe para organizar os dados do GUI
class GUIData:
    # Definição dos dados e inicialização do GUI
    def __init__(self, hora, fila, fila_atendimento, fila_atendidos):
        self.root = Tk()
        self.clock = None
        self.hora = StringVar()
        self.hora.set("20:{:02d}".format(hora))
        self.fila = fila
        self.frame_fila = None
        self.fila_atendimento = fila_atendimento
        self.frame_atendimento = None
        self.fila_atendidos = fila_atendidos
        self.frame_fila_atendidos = None
        self.boyImage = PhotoImage(file='res/boy3.gif')
        self.girlImage = PhotoImage(file='res/girl3.gif')

    # Função para realizar o update dos dados da fila
    def update(self, hora, fila, fila_atendimento, fila_atendidos):
        self.hora.set("20:{:02d}".format(hora))
        self.fila = fila
        self.criar_fila(self.frame_fila, self.fila)
        self.fila_atendimento = fila_atendimento
        self.criar_atendimento()
        self.fila_atendidos = fila_atendidos
        self.criar_fila(self.frame_fila_atendidos, self.fila_atendidos)
        self.root.update()

    # Função para atualizar os avatares da fila de espera e atendidos
    def criar_fila(self, frame, fila):
        for child in frame.winfo_children():
            child.destroy()
        for i in range(fila.quantidade_fila()):
            morador = fila.escolher_morador(i).morador
            valor = 0
            if frame == self.frame_fila:
                valor = "20:{:02d}".format(morador.hora_entrada)
            elif frame == self.frame_fila_atendidos:
                valor = "{:02d} min".format(morador.tempo_espera)
            child_frame = Frame(frame, width=60)
            child_frame.grid(column=i, row=1)
            if morador.genero == 0:
                Label(child_frame, image=self.girlImage).grid(row=0, column=0)
            elif morador.genero == 1:
                Label(child_frame, image=self.boyImage).grid(row=0, column=0)
            Label(child_frame, text=valor).grid(row=2, column=0)

    # Função que cria os 2 postos de atendimento, cada um com um máximo de 3 moradores atendidos
    def criar_atendimento(self):
        fila = self.fila_atendimento
        for child in self.frame_atendimento.winfo_children():
            child.destroy()
        child_frame_1 = LabelFrame(self.frame_atendimento, borderwidth=2, relief="ridge",
                                   text="Atendimento")
        child_frame_1.grid(column=0, row=0)
        child_frame_2 = None
        if fila.quantidade_fila() > 3:
            child_frame_2 = LabelFrame(self.frame_atendimento, borderwidth=2, relief="ridge",
                                       text="Atendimento Auxiliar")
            child_frame_2.grid(column=2, row=0)
        for i in range(fila.quantidade_fila()):
            morador = fila.escolher_morador(i).morador
            if i < 3:
                put_frame = Frame(child_frame_1, width=60)
                position = i
            else:
                put_frame = Frame(child_frame_2, width=60)
                position = i - 3
            put_frame.grid(column=position, row=0)
            if morador.genero == 0:
                Label(put_frame, image=self.girlImage).grid(row=0, column=0)
            elif morador.genero == 1:
                Label(put_frame, image=self.boyImage).grid(row=0, column=0)

    # Função que cria todos os elementos do GUI e a inicia
    def criar_gui(self):
        root = self.root
        root.minsize(600, 300)
        frm = ttk.Frame(root, padding=10)
        frm.grid(column=0, row=0, sticky="nsew")
        frm.grid_columnconfigure(10, weight=1)
        frm.grid_rowconfigure(10, weight=1)
        frm.grid()

        rm = StringVar()
        rm.set(str(96))
        max_fila = StringVar()
        max_fila.set(str(15))
        segundo = StringVar()
        segundo.set(str(0.2))
        min_segundo_atendente = StringVar()
        min_segundo_atendente.set(str(10))

        # Função para parar a simulação
        def parar():
            stop_sim()

        # Função para inicializar a simulação
        def simular():
            simular_fila(int(rm.get()), int(max_fila.get()), float(segundo.get()), int(min_segundo_atendente.get()),
                         self)

        # Botões de Controle e Relógio
        ttk.Button(frm, text="Simular", command=simular, padding=5).grid(column=1, row=0)
        ttk.Button(frm, text="Parar", command=parar, padding=5).grid(column=5, row=0)
        ttk.Label(frm, text="Hora:").grid(column=5, row=1)
        self.clock = Label(frm, textvariable=self.hora)
        self.clock.grid(column=6, row=1)

        # Frames das Filas
        # Frame da fila de espera
        self.frame_fila = ttk.LabelFrame(frm, padding=5, height=200, width=1200, borderwidth=2, relief="ridge",
                                          text="Fila de Espera")
        self.frame_fila.grid(columnspan=7, row=2, sticky="we")
        self.frame_fila.grid_propagate(False)
        # Frame das filas de atendimento
        self.frame_atendimento = ttk.Frame(frm, padding=5, height=200, width=1200)
        self.frame_atendimento.grid(columnspan=7, row=3)
        self.frame_atendimento.grid_propagate(False)
        # Frame da fila de atendidos
        self.frame_fila_atendidos = ttk.LabelFrame(frm, padding=5, height=200, width=1200, borderwidth=2,
                                                    relief="sunken", text="Atendidos")
        self.frame_fila_atendidos.grid(columnspan=7, row=4, sticky="we")
        self.frame_fila_atendidos.grid_propagate(False)

        # Controle de Variáveis
        ttk.Entry(frm, textvariable=segundo).grid(column=0, row=6)
        ttk.Label(frm, text="Máximo da fila:").grid(column=2, row=5)
        ttk.Entry(frm, textvariable=max_fila).grid(column=2, row=6)
        ttk.Label(frm, text="Segundo atendente:").grid(column=4, row=5)
        ttk.Entry(frm, textvariable=min_segundo_atendente).grid(column=4, row=6)
        ttk.Label(frm, text="RM:").grid(column=6, row=5)
        ttk.Entry(frm, textvariable=rm).grid(column=6, row=6)

        root.mainloop()
