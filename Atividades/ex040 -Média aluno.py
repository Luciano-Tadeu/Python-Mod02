n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2)/2

if media >= 7:
    print("Aluno APROVADO com média {}".format(media))
elif media >= 5 and media < 7:
    print("Aluno de RECUPERAÇÃO com média {}".format(media))
else:
    print("Aluno REPROVADO com média {}".format(media))