from random import randint

print("Sou seu computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinha qual foi?")
pal = int(input("Qual é seu palpite? "))
palPC = randint(0, 10)
cont = 1

while pal != palPC:
    cont += 1
    if pal < palPC:
        print("Mais... Tente mais uma vez.")
        pal = int(input("Qual é seu palpite? "))
    elif pal > palPC:
        print("Menos... Tente mais uma vez.")
        pal = int(input("Qual é seu palpite? "))
    
    
print("Acertou com {} tentativas. Parabéns!".format(cont))