print("="*10, "LOJAS LUCIANO", "="*10)

preco = float(input("Qual o preço do produto? R$"))

print("FORMAS DE PAGAMENTOS \n[ 1 ] À vista dinheiro/cheque \n[ 2 ] À vista no cartão \n[ 3 ] 2x sem juros no cartão \n[ 4 ] 3x ou mais com juros no cartão")

opcao = int(input("Qual a opção? "))

if opcao == 1:
    precoD = preco*0.9
elif opcao == 2:
    precoD = preco*0.95
elif opcao == 3:
    precoD = preco
    parcela = precoD / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opcao == 4:
    precoD = preco*1.2
    parcelas = int(input("Quantas parcelas? "))
    parcela = precoD / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f}".format(parcelas, parcela))
else:
    print("Opção Inválida!")
    
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, precoD))       