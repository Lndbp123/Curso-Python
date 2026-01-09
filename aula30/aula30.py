velocidade = 61 
local_carro = 100

RADAR_1 = 60 
LOCAL_1 = 100     
RADAR_RANGE = 1

if local_carro >= (local_carro - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    if velocidade > RADAR_1:
        print(f'Você foi multado por excesso de velocidade! Velocidade: {velocidade}km/h, Limite: {RADAR_1}km/h')
    else:
        print('Você está dentro do limite de velocidade. Tenha um bom dia!')