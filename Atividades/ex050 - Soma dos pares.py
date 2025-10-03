s = 0
i = 0
for c in range (0, 6):
    num = int(input("Digite um número "))
    if num % 2 == 0:
        s += num
        i += 1
print("A soma dos {} números pares informados é: {}".format(i, s))