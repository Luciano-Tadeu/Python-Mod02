num = int(input("Digite um número para ver sua tabuada: "))

for c in range(1, 11):
    mult = num*c
    print("{} x {} = {}".format(num, c, mult))