from datetime import date
ano = int(input("Digite o ano de nascimento do atleta: "))
hoje = date.today().year
idade = hoje - ano


if idade > 0 and idade <= 9:
    print("O atleta tem {} anos e é classficado como \033[0;33mMIRIM\033[m".format(idade))
elif idade > 9 and idade <= 14:
    print("O atleta tem {} anos e é classficado como \033[0;33mINFANTIL\033[m".format(idade))
elif idade > 14 and idade <= 19:
    print("O atleta tem {} anos e é classficado como \033[0;33mJUNIOR\033[m".format(idade))
elif idade > 19 and idade <= 25:
    print("O atleta tem {} anos e é classficado como \033[0;33mSÊNIOR\033[m".format(idade))
else:
    print("O atleta tem {} anos e é classficado como \033[0;33mMASTER\033[m".format(idade))