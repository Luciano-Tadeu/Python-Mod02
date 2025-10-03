num = int(input("Digite um número: "))
nDiv = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[0;32m{}\033[m".format(c), end=' ')
        nDiv += 1
    else:
        print("\033[0;31m{}\033[m".format(c), end=' ')
        
print("\nO número {} foi divisível {} vezes".format(num, nDiv))

if nDiv == 2:
    print("E por isso o número é PRIMO!")
else:
    print("E por isso o número é NÃO É PRIMO!")