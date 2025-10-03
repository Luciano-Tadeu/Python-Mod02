peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso/(pow(altura, 2))

print("O IMC dessa pessoa é de {:.2f}".format(imc))

if imc < 18.5:
    print("ATENÇÃO, você está na faixa ABAIXO DE PESO NORMAL!")
elif imc >= 18.5 and imc < 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL!")
elif imc >= 25 and imc < 30:
    print("ATENÇÃO, você está na faixa de EXCESSO DE PESO!")
elif imc >= 30 and imc < 35:
    print("ATENÇÃO, você está na faixa OBESIDADE 1!")
elif imc >= 35 and imc < 40:
    print("ATENÇÃO, você está na faixa OBESIDADE 2!")
else:
    print("ATENÇÃO, você está na faixa OBESIDADE 3!")