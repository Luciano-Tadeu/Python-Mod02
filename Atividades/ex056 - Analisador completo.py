somaIdades = 0
iMaisVelho = 0
hMaisVelho = ''
contMulheresNovas = 0

for c in range(1, 5):
    print("----- {}ª PESSOA -----".format(c))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    somaIdades += idade
    if iMaisVelho < idade:
        iMaisVelho = idade
        hMaisVelho = nome
    if idade < 20 and sexo == 'F':
        contMulheresNovas += 1

mediaIdades = somaIdades/4
print("A média de idade do grupo é de {:.2f} anos".format(mediaIdades))
print("O homem mais velho tem {} anos e se chama {}".format(iMaisVelho, hMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(contMulheresNovas))