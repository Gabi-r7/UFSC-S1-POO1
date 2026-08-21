hora_inicio, hora_termino = map(int, input('Digite a hora inicial e final do jogo (separado por espaços): ').split())

if hora_inicio == hora_termino:
	duracao_jogo = 24
elif hora_inicio < hora_termino:
	duracao_jogo = hora_termino - hora_inicio
else:
	duracao_jogo = (24 - hora_inicio) + hora_termino
    
print(f'O JOGO DUROU {duracao_jogo} HORA(S)')
