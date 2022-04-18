import time
from random import random
from fila import Fila
from morador import Morador

# Constantes de tempo
ns_segundo = 1000000000
segundo_simulado = 0.5
rodando = False


# função para arrumar a frase caso tenha apenas 1 morador
def corrigir_frase(quantidade):
    if quantidade > 1:
        return "moradores estão"
    elif quantidade == 1:
        return "morador está"


def printar_info(tempo_agora, fila, fila_em_atendimento, fila_atendidos):
    numero_atendidos = fila_atendidos.quantidade_fila()
    numero_na_fila = fila.quantidade_fila()
    numero_em_atendimento = fila_em_atendimento.quantidade_fila()
    # Printamos a hora atual para acompanhar
    print("Hora: 20:{:02d}".format(tempo_agora))
    # Printamos a quantidade de moradores na fila e quantos foram atendidos
    print("Estão na fila {} moradores, foram atendidos {}.".format(numero_na_fila, numero_atendidos))
    # Printamos quantos estão atendidos agora, caso ninguém esteja sendo atendido informamos isso
    if numero_em_atendimento == 0:
        print("Ninguém está em atendimento!")
    else:
        print("No momento {} {} em atendimento.".format(numero_em_atendimento,
                                                        corrigir_frase(numero_em_atendimento)))
    # Printamos quanto demorou cada morador para ser atendido, caso ainda não tenha sido atendido, informamos isso
    if numero_atendidos == 0:
        print("Ainda não foi atendido nenhum morador!")
    else:
        print("O tempo de espera de cada morador atendido foi respectivamente {}minutos.".format(
            fila_atendidos.tempo_atendimento()))


def stop_sim():
    global rodando
    rodando = False


def simular_fila(rm, max_fila, segundo, minimo_para_auxiliar, data):
    global rodando
    # calculo do tempo para servir baseado no RM
    tempo_servir = rm % 3 + 1
    # randomizamos os moradores do início da fila
    moradores_inicio_fila = int(random() * max_fila - 1) + 1
    inicio = time.time_ns()
    contador_servir = 0
    tempo_atual = 0
    tempo = 0
    # Criamos a fila de espera e a fila de atendidos e da que está em atendimento
    fila_espera = Fila(max_fila)
    em_atendimento = Fila(None)
    atendidos = Fila(None)
    # Enfileiramos os primeiros da fila
    fila_espera.fila_inicial(tempo, moradores_inicio_fila)
    rodando = True

    def servir_pratos():
        # Os pratos a serem atendidos são 3 por vez, exceto quando a fila estiver menor que 3
        pratos_servidos = 3
        if fila_espera.quantidade_fila() < 3:
            pratos_servidos = fila_espera.quantidade_fila()
        for n in range(pratos_servidos):
            morador_atendido = fila_espera.servir_morador(tempo)
            em_atendimento.enfileirar(morador_atendido)

    # Printamos a informação inicial
    printar_info(tempo, fila_espera, em_atendimento, atendidos)
    # Definimos como ‘loop’ o while até a fila a ser atendida ser zerada
    while fila_espera.quantidade_fila() > 0 or em_atendimento.quantidade_fila() != 0 and rodando:
        agora = time.time_ns()
        if agora > inicio + segundo * ns_segundo:
            # Adicionamos ao tempo o valor de 1
            tempo += 1
            inicio = agora
            for i in range(em_atendimento.quantidade_fila()):
                atendido = em_atendimento.sair_da_fila()
                atendidos.enfileirar(atendido)
            # A cada 2 minutos, um morador entra na fila, coloquei uma opção para caso só tenha um morador em
            # atendimento não entrar mais ninguém da fila, pois senão entrava em um ‘loop’ infinito
            if tempo % 2 == 0 and em_atendimento.quantidade_fila() != 1:
                novo_morador = Morador(tempo)
                fila_espera.enfileirar(novo_morador)
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
                # Printamos as informações atualizadas
                printar_info(tempo, fila_espera, em_atendimento, atendidos)
                data.update(tempo, fila_espera, em_atendimento, atendidos)


# simular_fila(96, 15, segundo_simulado, 10)
