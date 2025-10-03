valorCasa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o valor do seu salário? "))
tempoAnos = int(input("Em quantos anos gostaria de pagar? "))

presMensal = valorCasa/(tempoAnos * 12)

print("A casa no valor de {} terá uma parcela mensal de {:.2f}".format(valorCasa, presMensal))

if sal*0.3 >= presMensal:
    print("Empréstimo concedido")
else:
    print("Empréstimo negado")