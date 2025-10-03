print('='*20, '\n10 TERMOS DE UMA PA')
print('='*20)

pTermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decPriTermo = pTermo + (11 - 1)*razao

for c in range (pTermo, decPriTermo, razao):
    print("{} ->".format(c), end=' ')
print("ACABOU")