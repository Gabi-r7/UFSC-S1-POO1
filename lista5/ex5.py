tentativas = int(input('Digite quantas tentativas o garçom realizou: '))
quebrados = 0

for i in range(tentativas):
    l, c = map(int, input('Digite os valores de latas e copos: ').split())

    if l > c:
        quebrados += c

print(quebrados)