print("GERADOR DE PA \n", "-="*10)
a1 = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))
n = int(input("Digite até que termo gostaria: "))

c = 1

while c <= n:
    print("{},".format(a1) if c != n else "{}.".format(a1), end=' ')
    a1 += r
    c += 1