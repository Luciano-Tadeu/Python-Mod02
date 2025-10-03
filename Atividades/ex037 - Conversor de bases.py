num = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha uma das bases para conversão: \n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL \nSua opção: "))

if opcao == 1:
    print("{} convertido para BINÁRIO é {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")
    