n = int(input())

l1 = 2
l2 = 5
l3 = 5
l4 = 4
l5 = 5
l6 = 6
l7 = 3
l8 = 7
l9 = 6
l0 = 6

for i in range(n):
    string = input()

    quant_leds = 0
    for i in range(len(string)):
        if string[i] == "0":
            quant_leds += l0
        elif string[i] == "1":
            quant_leds += l1
        elif string[i] == "2":
            quant_leds += l2
        elif string[i] == "3":
            quant_leds += l3
        elif string[i] == "4":
            quant_leds += l4
        elif string[i] == "5":
            quant_leds += l5
        elif string[i] == "6":
            quant_leds += l6
        elif string[i] == "7":
            quant_leds += l7
        elif string[i] == "8":
            quant_leds += l8
        elif string[i] == "9":
            quant_leds += l9
    
    print(quant_leds, 'leds')
        