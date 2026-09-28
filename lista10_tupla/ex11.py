string = input('Digite uma palavra: ').upper()
pontos = 0

for i in range(len(string)):
    if string[i] == 'Q' or string[i] == 'Z':
        pontos += 10
    elif string[i] == 'J' or string[i] == 'X':
            pontos += 8
    elif string[i] == 'K':
        pontos += 5
    elif string[i] == 'F' or string[i] == 'H' or string[i] == 'V' or string[i] == 'W' or string[i] == 'Y':
            pontos += 4
    elif string[i] == 'B' or string == 'C' or string[i] == 'M' or string[i] == 'P':
            pontos += 3
    elif string[i] == 'D' or string == 'G':
            pontos += 2

print(pontos)
