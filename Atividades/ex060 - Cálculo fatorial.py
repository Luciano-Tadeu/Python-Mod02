num = int(input("Digite um número para calcular seu fatorial: "))
mult = 1
print("O cálculo de {}! é ".format(num), end=' ')

while num > 0:
    print("{}".format(num), end = ' ')
    print(" x " if num > 1 else " = ", end=' ')
    mult *= num
    num -= 1

print("{}".format(mult))