# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

idadeLida = int(input('Digite sua idade em dias: '))

idadeAnos = idadeLida // 365
idadeLida -= idadeAnos * 365
idadeMes = idadeLida // 30
idadeLida -= idadeMes * 30
idadeDias = idadeLida

print(f'Sua idade é de: \n{idadeAnos} ano(s)\n{idadeMes} mes(es)\n{idadeDias} dia(s)')