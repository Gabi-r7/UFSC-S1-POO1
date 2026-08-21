dia_inicio = int(input('Digite o dia de início do evento: '))
hora_inicio = int(input('Digite a hora de início do evento: '))
minuto_inicio = int(input('Digite o minuto de início do evento: '))
segundo_inicio = int(input('Digite o segundo de início do evento: '))

dia_fim = int(input('Digite o dia de fim do evento: '))
hora_fim = int(input('Digite a hora de fim do evento: '))
minuto_fim = int(input('Digite o minuto de fim do evento: '))
segundo_fim = int(input('Digite o segundo de fim do evento: '))

inicio_em_segundos = segundo_inicio + (minuto_inicio * 60) + (hora_inicio * 60 * 60) + (dia_inicio * 24 * 60 * 60)
fim_em_segundos = segundo_fim + (minuto_fim * 60) + (hora_fim * 60 * 60) + (dia_fim * 24 * 60 * 60)
duracao_total_segundos = fim_em_segundos - inicio_em_segundos

duracao_dias = duracao_total_segundos // 86400
duracao_total_segundos %= 86400
duracao_horas = duracao_total_segundos // 3600
duracao_total_segundos %= 3600
duracao_minutos = duracao_total_segundos // 60
duracao_total_segundos %= 60
duracao_segundos = duracao_total_segundos

print(f'Duração total: {duracao_dias} dia(s), {duracao_horas} hora(s), {duracao_minutos} minuto(s) e {duracao_segundos} segundo(s).')

