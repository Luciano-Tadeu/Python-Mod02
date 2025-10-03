from datetime import date

anoAtual = date.today().year
contMaiores = 0
contMenores = 0

for c in range(0, 7):
    
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c+1)))
    
    if anoAtual - ano < 18:
        contMenores += 1
    else:
        contMaiores += 1

print("Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade".format(contMaiores, contMenores))