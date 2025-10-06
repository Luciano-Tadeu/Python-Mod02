n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
fim = False

while not fim:
    print("[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa")
    escolha = int(input(">>>>>>>>>>> Qual é a sua opção? "))
    
    if escolha == 1:
        soma = n1 + n2
        print("{} + {} = {}".format(n1, n2, soma))
    elif escolha == 2:
        mult = n1*n2
        print("{} x {} = {}".format(n1, n2, mult))
    elif escolha == 3:
        if n1 > n2:
            print("O {} é o maior".format(n1))
        elif n2 > n1:
            print("O {} é o maior".format(n2))
        else:
            print("Os números são iguais")
    elif escolha == 4:
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    elif escolha == 5:
        fim = True
    else:
        print("Opção inválida!")
    