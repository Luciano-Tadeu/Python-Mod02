from time import sleep
from random import randint


print("Sua opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA")
jogada = int(input("Qual é a sua jogada? "))
jogadaPC = randint(0, 2)


print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
    
if jogada == 0:
    jEsc = 'PEDRA'
elif jogada == 1:
    jEsc = 'PAPEL'
elif jogada == 2:
    jEsc = 'TESOURA'
else:
    print("Jogada INVÁLIDA!")
    exit()

if jogadaPC == 0:
    jEscPC = 'PEDRA'
elif jogadaPC == 1:
    jEscPC = 'PAPEL'
elif jogadaPC == 2:
    jEscPC = 'TESOURA'

print("-="*20)
print("Computador jogou {}".format(jEscPC))
print("Jogador jogou {}".format(jEsc))
print("-="*20)

if jogada == jogadaPC:
    print("EMPATE!")
elif jogada == 0 and jogadaPC == 1:
    print("COMPUTADOR VENCEU!")
elif jogada == 0 and jogadaPC == 2:
    print("JOGADOR VENCEU!")
elif jogada == 1 and jogadaPC == 0:
    print("JOGADOR VENCEU!")
elif jogada == 1 and jogadaPC == 2:
    print("COMPUTADOR VENCEU!")
elif jogada == 2 and jogadaPC == 0:
    print("COMPUTADOR VENCEU!")
else:
    print("JOGADOR VENCEU!")