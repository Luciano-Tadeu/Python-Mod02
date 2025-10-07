print('-'*20, "\nLOJA SUPER BARATÃO\n", '-'*20)

toCompra = 0
toProdutos1000 = 0

while True:
    nome = input("Nome do Produto: ")
    preço = 0
    while preço <= 0:
        preço = float(input("Preço: R$"))
        
    continuar = ' '
    
    if toCompra == 0:
        produtoBarato = nome
        preçoBarato = preço
    
    toCompra += preço
    
    if preço >= 1000:
        toProdutos1000 += 1
    
    
    if preço < preçoBarato:
        produtoBarato = nome
        preçoBarato = preço
    
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar == 'N':
        break

print("-----------------------------FIM DO PROGRAMA-----------------------------")
print("O total da compra foi de R${:.2f}".format(toCompra))
print("Temos {} produtos custando mais de R$1000.00".format(toProdutos1000))
print("O produto mais barato foi {} que custa R${:.2f}".format(produtoBarato, preçoBarato))