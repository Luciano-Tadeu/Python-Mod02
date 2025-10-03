s = 0
i = 0
for c in range(0, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
            i += 1
            
print("A soma dos {} ímpares múltiplos de 3 é: {}".format(i, s))