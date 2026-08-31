a = float(input("Preço do álcool: "))
g = float(input("Preço da gasolina: "))
ra = float(input("Rendimento com álcool: "))
rg = float(input("Rendimento com gasolina: "))

custo_alcool = a / ra
custo_gasolina = g / rg

if custo_alcool < custo_gasolina:
    print("A")
else:
    print("G")
