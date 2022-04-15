# Classe que contem as informações do morador
class Morador:
    # Definição do morador, define o horário de entrada, se ele já foi atendido e o tempo de espera até atendimento
    def __init__(self, hora_entrada):
        self.hora_entrada = hora_entrada
        self.atendido = False
        self.tempo_espera = 0

    def foi_atendido(self, tempo_agora):
        self.atendido = True
        self.tempo_espera = tempo_agora - self.hora_entrada
