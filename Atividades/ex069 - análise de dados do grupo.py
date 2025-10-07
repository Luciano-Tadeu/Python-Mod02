cIdade = 0
cSexo = 0
cMulher = 0

while True:
    print('-'*20)
    print("CADASTRE UMA PESSOA")
    print('-'*20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input("Sexo: [M/F] ").upper().strip()[0]
    print('-'*20)
    if idade >= 18:
        cIdade += 1
    if sexo in 'mM':
        cSexo += 1
    if sexo in 'fF' and idade <= 20:
        cMulher += 1
    cont = ' '
    while cont not in 'SN':
        cont = input("Quer continuar? [S/N] ").upper().strip()[0]
    if cont == "N":
        break

print("Total de pessoas com mais de 18 anos: {}".format(cIdade))
print("Ao todo temos {} homens cadastrados".format(cSexo))
print("E temos {} mulheres com menos de 20 anos".format(cMulher))