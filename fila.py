from morador import Morador


# Classe para o controle da fila
class Fila:
    # Classe nodo da fila
    class Nodo:
        def __init__(self, morador, seguinte=None):
            self.morador = morador
            self.seguinte = seguinte

        def __str__(self):
            return str(self.morador)

    # Definição da fila
    def __init__(self, tamanho_max):
        self.inicio = None
        self.tamanho_max = tamanho_max

    # Criação da fila inicial baseada no tamanho random
    def fila_inicial(self, hora, tamanho):
        for i in range(tamanho):
            morador = Morador(hora)
            self.enfileirar(morador)

    # função para colocar um novo morador na fila até um máximo de 15, caso seja maior, não entra na fila
    def enfileirar(self, morador):
        nodo = self.Nodo(morador)
        if self.tamanho_max is None or self.quantidade_fila() < self.tamanho_max:
            if self.inicio is None:
                self.inicio = nodo
            elif self.inicio.seguinte is None:
                self.inicio.seguinte = nodo
            else:
                fim = self.encontrar_fim()
                fim.seguinte = nodo

    # função para selecionar um morador da fila
    def servir_morador(self, hora_atendida):
        if not self.fila_vazia():
            nodo = self.inicio
            self.inicio = nodo.seguinte
            nodo.morador.foi_atendido(hora_atendida)
            return nodo.morador

    # função para selecionar um morador da fila
    def escolher_morador(self, index):
        i = 0
        nodo = self.inicio
        while i < index:
            i += 1
            nodo = nodo.seguinte
        return nodo

    def encontrar_fim(self):
        nodo = self.inicio
        while nodo.seguinte is not None:
            nodo = nodo.seguinte
        return nodo

    # função que verifica se a fila está vazio
    def fila_vazia(self):
        return self.inicio is None

    # função que retorna a quantidade de moradores na fila
    def quantidade_fila(self):
        tamanho = 0
        nodo = self.inicio
        while nodo is not None:
            tamanho += 1
            nodo = nodo.seguinte
        return tamanho

    def tempo_atendimento(self):
        lista_tempo_atendimento = ""
        for i in range(self.quantidade_fila()):
            morador = self.escolher_morador(i).morador
            if morador.atendido:
                lista_tempo_atendimento += str(morador.tempo_espera) + " "
        return lista_tempo_atendimento
