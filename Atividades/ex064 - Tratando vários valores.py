n = 0
s = 0
cont = -1
while n != 999:
    n = int(input("Digite um número [999 pra parar]: "))
    s += n
    cont += 1
s -= 999
print("Você digitou {} números e a soma entre eles foi {}.".format(cont, s))