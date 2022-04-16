import time
from random import random
from fila import Fila
from morador import Morador

# from GUI import *

# calculo do tempo para servir baseado no RM
tempo_servir = 96 % 3 + 1
# randomizamos os moradores do início da fila
max_fila = 40
moradores_inicio_fila = int(random() * max_fila-1) + 1
inicio = time.time_ns()
segundo = 1000000000
segundo_simulado = 2
tempo = 0
tempo_atual = 0
contador_servir = 0
minimo_para_auxiliar = 10


def printar_info(tempo_agora, fila, fila_atendidos):
    # Printamos a hora atual para acompanhar
    print("Hora: 20:{:02d}".format(tempo_agora))
    # Printamos a quantidade de moradores na fila e quantos foram atendidos
    print("Estão na fila {} moradores, foram atendidos {}.".format(fila.quantidade_fila(),
                                                                   fila_atendidos.quantidade_fila()))
    # Printamos quanto demorou cada morador para ser atendido, caso ainda não tenha sido atendido, informamos isso
    if fila_atendidos.quantidade_fila() == 0:
        print("Ainda não foi atendido nenhum morador!")
    else:
        print("O tempo de espera de cada morador atendido foi de {}minutos respectivamente".format(
            fila_atendidos.tempo_atendimento()))


def servir_pratos():
    # Os pratos a serem atendidos são 3 por vez, exceto quando a fila estiver menor que 3
    pratos_servidos = 3
    if fila_espera.quantidade_fila() < 3:
        pratos_servidos = fila_espera.quantidade_fila()
    for i in range(pratos_servidos):
        atendido = fila_espera.servir_morador(tempo)
        atendidos.enfileirar(atendido)


# Criamos a fila de espera e a fila de atendidos
fila_espera = Fila(max_fila)
atendidos = Fila(None)
# Enfileiramos os primeiros da fila
fila_espera.fila_inicial(tempo, moradores_inicio_fila)

# Printamos a informação inicial
printar_info(tempo, fila_espera, atendidos)

# Definimos como ‘loop’ o while até a fila a ser atendida ser zerada
while fila_espera.quantidade_fila() > 0:
    agora = time.time_ns()
    if agora > inicio + segundo_simulado * segundo:
        # Adicionamos ao tempo o valor de 1
        tempo += 1
        inicio = agora
    # se o tempo for maior que 10, iniciamos os atendimentos
    if tempo != tempo_atual:
        tempo_atual = tempo
        if tempo >= 10:
            tempo_atual = tempo
            # este contador serve para definir o tempo apara o atendimento
            contador_servir += 1
            # caso o contador seja maior que o tempo definido pelo RM, façamos os atendimentos
            if contador_servir >= tempo_servir:
                contador_servir = 0
                servir_pratos()
                # Se a fila estiver maior que 10, o auxiliar ira fazer os atendimentos também
                if fila_espera.quantidade_fila() > minimo_para_auxiliar:
                    servir_pratos()
        # A cada 2 minutos, um morador entra na fila
        if tempo % 2 == 0:
            novo_morador = Morador(tempo)
            fila_espera.enfileirar(novo_morador)
        # Printamos as informações atualizadas
        printar_info(tempo, fila_espera, atendidos)
