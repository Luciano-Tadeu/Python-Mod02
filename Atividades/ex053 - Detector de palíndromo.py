frase = input("Digite um frase: ").upper().strip().replace(" ", "")
fraseINV = ""

for c in range(len(frase) - 1, -1, -1):
    fraseINV += frase[c]
    
print("O inverso de {} é {}".format(frase, fraseINV))
if frase == fraseINV:
    print("A frase digitada é um palíndromo")
else:
    print("A frase digitada não é um palíndromo")