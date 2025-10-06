print("GERADOR DE PA \n", "-="*10)
a1 = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))
i = 1
c = 1

while c <= 10:
    print(" {} ->".format(a1) if c != 10 else " {} -> PAUSA ".format(a1), end='')
    a1 += r
    c += 1

while i != 0:
    n = int(input("\nQuantos termos você quer mostrar a mais? "))

    if n == 0:
        print("Progressão finalizada com {} termos mostrados".format(c-1))
        i -= 1
    else:
        novoNum = (c-1) + n
        while c <= novoNum:
            print(" {} -> ".format(a1) if c != novoNum else " {} -> PAUSA ".format(a1), end='')
            a1 += r
            c += 1