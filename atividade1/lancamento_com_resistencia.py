Web VPython 3.2

# Configuração da cena
scene.background = vector(0.8, 0.8, 0.8)  # Cor de fundo cinza claro
scene.width = 800
scene.height = 600

# Criando a esfera com arrasto (cor azul)
bola_com_arrasto = sphere(pos=vector(-1, 0.6, 0), radius=0.5, color=color.blue, make_trail=True)

# Criando a esfera sem arrasto (cor vermelha)
bola_sem_arrasto = sphere(pos=vector(1, 0.6, 0), radius=0.5, color=color.red, make_trail=True)

# Parâmetros do sistema
m = 1.0  # Massa do objeto (kg)
g = 9.8  # Aceleração gravitacional (m/s^2)
coeficiente_arrasto_humano = 0.47  # Coeficiente de arrasto (kg/s)
v_com_arrasto = vector(0, 20, 0)  # Velocidade inicial da bola com arrasto (m/s)
v_sem_arrasto = vector(0, 20, 0)  # Velocidade inicial da bola sem arrasto (m/s)

# Criando uma linha de referência horizontal
referencia_com_arrasto = cylinder(pos=vector(-5, bola_com_arrasto.pos.y, 0), axis=vector(10, 0, 0), radius=0.05, color=color.green)

# Criando um plano de fundo para representar o chão
chao = box(pos=vector(0, 0, 0), size=vector(10, 0.1, 10), color=color.gray(0.5))

# Vetores de força para a bolinha com arrasto
f_gravitacional_com_arrasto = arrow(pos=bola_com_arrasto.pos, axis=vector(0, -m*g, 0), color=color.yellow, shaftwidth=0.1)
f_arrasto = arrow(pos=bola_com_arrasto.pos, axis=vector(0, 0, 0), color=color.red, shaftwidth=0.1)

dt = 0.01  # Intervalo de tempo (s)
# Inicialização do tempo
tempo_inicio = clock()
# Simulação
while bola_com_arrasto.pos.y > bola_com_arrasto.radius or bola_sem_arrasto.pos.y > bola_sem_arrasto.radius:
    rate(100)

    # Força gravitacional
    f_gravidade = vector(0, -m*g, 0)

    # Para a bolinha com arrasto
    if bola_com_arrasto.pos.y > bola_com_arrasto.radius:
        f_arrasto_valor = -coeficiente_arrasto_humano * v_com_arrasto  # Força de arrasto
        f_total_com_arrasto = f_gravidade + f_arrasto_valor  # Força total atuando na bolinha com arrasto
        aceleracao_com_arrasto = f_total_com_arrasto / m
        v_com_arrasto += aceleracao_com_arrasto * dt
        bola_com_arrasto.pos += v_com_arrasto * dt

        # Atualizar vetores de força
        f_gravitacional_com_arrasto.pos = bola_com_arrasto.pos
        f_arrasto.pos = bola_com_arrasto.pos
        f_arrasto.axis = f_arrasto_valor  # Atualiza direção e magnitude do vetor de arrasto

        # Atualizar a linha de referência
        referencia_com_arrasto.pos.y = bola_com_arrasto.pos.y  # A linha de referência se move junto com a bolinha com arrasto
            # Parar a bolinha vermelha quando atingir o chão 
        if bola_com_arrasto.pos.y <= bola_com_arrasto.radius:
            print('Bola com arrasto colidiu com o chão em tempo:',   clock() - tempo_inicio, 'segundos')
            v_com_arrasto = vector(0, 0, 0)  # Define a velocidade como zero para parar o movimento
            
        valor_de_imprecisao = 0.05 # o calculo não é exato, então é considerar certa imprecisão
        if (abs(v_com_arrasto.y) <= valor_de_imprecisao and bola_com_arrasto.pos.y > 0.6):
            print('Bola com arrasto chegou na altura máxima em tempo:', clock() - tempo_inicio, 'segundos')
            print('altura máxima =', bola_com_arrasto.pos.y, 'metros')


    # Para a bolinha sem arrasto
    if bola_sem_arrasto.pos.y > bola_sem_arrasto.radius:
        f_total_sem_arrasto = f_gravidade  # Apenas a força gravitacional atua na bolinha sem arrasto
        aceleracao_sem_arrasto = f_total_sem_arrasto / m
        v_sem_arrasto += aceleracao_sem_arrasto * dt
        bola_sem_arrasto.pos += v_sem_arrasto * dt

        # Parar a bolinha vermelha quando atingir o chão
        if bola_sem_arrasto.pos.y <= bola_sem_arrasto.radius:
            print('Bola sem arrasto colidiu em tempo:', clock() - tempo_inicio, 'segundos' )
            v_sem_arrasto = vector(0, 0, 0)  # Define a velocidade como zero para parar o movimento
