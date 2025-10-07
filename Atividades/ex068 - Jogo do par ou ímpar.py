from random import randint

perdeu = False
contV = 0

while perdeu == False:
    print("=-="*20)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-="*20)
    num = int(input("Diga um valor: "))
    numPC = randint(1, 10)
    parOUimpar = input("Par ou Ímpar? [P/I] ").upper().strip()[0]
    resultado = numPC + num
    print("-"*40)
    print("Você jogou {} e o computador {}. Total de {}".format(num, numPC, resultado), end=' ')
    if resultado % 2 == 0:
        print("DEU PAR")
        if parOUimpar in 'pP':
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            contV += 1
        else:
            print("Você PERDEU!")
            perdeu = True
    else:
        print("DEU ÍMPAR")
        if parOUimpar in 'iI':
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            contV += 1
        else:
            print("Você PERDEU!")
            perdeu = True
print("=-="*40)
print(f"GAME OVER! Você venceu {contV} vezes")