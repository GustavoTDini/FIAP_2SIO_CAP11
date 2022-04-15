import time
from random import random
from fila import Fila
from morador import Morador

tempo_servir = 98 % 3 + 1
moradores_inicio_fila = int(random() * 14) + 1
agora = time.gmtime()[4]
tempo = 0
contador_servir = 0

fila_espera = Fila(True)
atendidos = Fila(False)
fila_espera.fila_inicial(tempo, moradores_inicio_fila)

print(moradores_inicio_fila)
print(fila_espera.quantidade_fila())
print(atendidos.quantidade_fila())

while fila_espera.quantidade_fila() >0:
    print("Hora: 20:{:02d}".format(tempo))
    tempo += 1
    if tempo > 10:
        contador_servir += 1
        if contador_servir >= tempo_servir:
            contador_servir = 0
            pratos_servidos = 3
            if fila_espera.quantidade_fila() < 3:
                pratos_servidos = fila_espera.quantidade_fila()
            for i in range(pratos_servidos):
                atendido = fila_espera.servir_morador(tempo)
                atendidos.enfileirar(atendido)
            if fila_espera.quantidade_fila() > 10:
                pratos_servidos = 3
                if fila_espera.quantidade_fila() < 3:
                    pratos_servidos = fila_espera.quantidade_fila()
                for i in range(pratos_servidos):
                    atendido = fila_espera.servir_morador(tempo)
                    atendidos.enfileirar(atendido)
    if tempo % 2 == 0:
        novo_morador = Morador(tempo)
        fila_espera.enfileirar(novo_morador)
    print("Estão na fila {} moradores, foram atendidos {}".format(fila_espera.quantidade_fila(),
                                                                  atendidos.quantidade_fila()))
    if atendidos.quantidade_fila() == 0:
        print("Ainda não foi atendido nenhum morador")
    else:
        print("O tempo de espera de cada morador atendido foi de {} minutos".format(atendidos.tempo_atendimento()))



