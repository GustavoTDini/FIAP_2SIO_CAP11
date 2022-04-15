from morador import Morador


# Classe para o controle da fila
class Fila:
    # Definição da fila
    def __init__(self, fila_espera):
        self.fila = []
        self.fila_espera = fila_espera

    def fila_inicial(self, hora, tamanho):
        for i in range(tamanho):
            morador = Morador(hora)
            self.enfileirar(morador)

    # função para colocar um novo morador na fila até um máximo de 15, caso seja maior, não entra na fila
    def enfileirar(self, morador):
        if not self.fila_espera or self.quantidade_fila() < 15:
            self.fila.append(morador)

    # função para selecionar um morador da fila
    def servir_morador(self, hora_atendida):
        if not self.fila_vazia():
            self.fila[0].foi_atendido(hora_atendida)
            morador = self.fila[0]
            self.fila.pop(0)
            return morador

    # função para selecionar um morador da fila
    def escolher_morador(self, index):
        return self.fila[index]

    # função que verifica se a fila está vazio
    def fila_vazia(self):
        return not self.fila

    # função que retorna a quantidade de moradores na fila
    def quantidade_fila(self):
        return len(self.fila)

    def tempo_atendimento(self):
        lista_tempo_atendimento = ""
        for i in range(self.quantidade_fila()):
            if self.escolher_morador(i).atendido:
                lista_tempo_atendimento += str(self.fila[i].tempo_espera) + " "
        return lista_tempo_atendimento

