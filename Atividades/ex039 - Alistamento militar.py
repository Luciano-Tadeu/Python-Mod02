import datetime
ano = int(input("Ano de nascimento: "))
hoje = datetime.date.today().year
idade = hoje - ano
print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, hoje))
if idade > 18 and idade < hoje:
    saldo = idade - 18
    print("Você deveria ter se alistado a {} anos.".format(saldo))   
    anoAlistar = hoje - saldo
    print("Seu alistamento deveria ter ocorrido em {}".format(anoAlistar))
elif idade < 18:
    saldo = -(idade - 18)
    print("Faltam {} anos para o seu alistamento.".format(saldo))
    anoAlistar = hoje + saldo
    print("Seu alistamento será em {}".format(anoAlistar))
elif idade == 18:
    print("Seu alistamento será AGORA em {}".format(hoje))
else:
    print("Idade inválida!")