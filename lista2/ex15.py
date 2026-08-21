hora_inicio, minuto_inicio, hora_termino, minuto_termino = map(int, input('Digite a hora e minutos iniciais e finais do jogo hora e minutos finais: ').split())
duracao_horas, duracao_minutos = 0, 0

if minuto_inicio != minuto_termino:
    if (minuto_inicio < minuto_termino):
        duracao_minutos = minuto_termino - minuto_inicio
    else:
        duracao_minutos = (60 - minuto_inicio) + minuto_termino
        duracao_horas -= 1
if hora_inicio == hora_termino and minuto_inicio == minuto_termino:
	duracao_horas = 24
elif hora_inicio < hora_termino:    
    duracao_horas += hora_termino - hora_inicio
else:
	duracao_horas = (24 - hora_inicio) + hora_termino
    
print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
