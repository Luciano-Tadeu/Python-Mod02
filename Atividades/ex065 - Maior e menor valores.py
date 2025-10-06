sair = "S"
maior = 0
menor = 0
soma = 0
p = 0
while sair in "sS":
    num = float(input("Digite um número: "))
    if p == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    p += 1
    sair = input("Quer continuar? [S/N] ").upper().strip()[0]

media = soma/p

print("Você digitou {} números e a média foi {:.2f}".format(p, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))